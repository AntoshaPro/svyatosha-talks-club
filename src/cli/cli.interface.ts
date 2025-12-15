import * as readline from 'readline';
import { GeminiService } from '../services/gemini.service';
import { ConfigManager } from '../config/config.manager';

export class CliInterface {
  private configManager: ConfigManager;
  private rl: readline.Interface;

  constructor() {
    this.configManager = new ConfigManager();
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
  }

  /**
   * Start the CLI interface
   */
  async start(): Promise<void> {
    console.log('=== Gemini API Client CLI ===');
    console.log('Commands:');
    console.log('  /help     - Show this help message');
    console.log('  /models   - List available models');
    console.log('  /setkey   - Set your API key');
    console.log('  /model    - Change the current model');
    console.log('  /quit     - Exit the application');
    console.log('');
    
    // Check if API key is configured
    const config = this.configManager.getConfig();
    if (!config.apiKey) {
      console.log('⚠️  No API key configured. Please use /setkey to enter your API key.');
      await this.handleSetKey();
    } else {
      console.log(`✅ API key is configured. Current model: ${config.selectedModel}`);
    }

    await this.runLoop();
  }

  /**
   * Main loop for CLI interaction
   */
  private async runLoop(): Promise<void> {
    while (true) {
      const input = await this.question('\nYou: ');
      
      if (input.startsWith('/')) {
        await this.handleCommand(input);
      } else {
        await this.handleChat(input);
      }
    }
  }

  /**
   * Handle commands
   */
  private async handleCommand(command: string): Promise<void> {
    switch (command.toLowerCase()) {
      case '/help':
        this.showHelp();
        break;
      case '/models':
        await this.showModels();
        break;
      case '/setkey':
        await this.handleSetKey();
        break;
      case '/model':
        await this.handleChangeModel();
        break;
      case '/quit':
      case '/exit':
        console.log('Goodbye!');
        process.exit(0);
        break;
      default:
        console.log(`Unknown command: ${command}. Type /help for available commands.`);
    }
  }

  /**
   * Handle chat messages
   */
  private async handleChat(message: string): Promise<void> {
    const config = this.configManager.getConfig();
    
    if (!config.apiKey) {
      console.log('❌ No API key configured. Please use /setkey to enter your API key.');
      return;
    }

    try {
      console.log('...');
      const geminiService = new GeminiService(config.apiKey);
      const response = await geminiService.generateText(message, config.selectedModel);
      console.log(`Gemini (${config.selectedModel}): ${response}`);
    } catch (error) {
      console.error(`❌ Error: ${(error as Error).message}`);
    }
  }

  /**
   * Handle setting API key
   */
  private async handleSetKey(): Promise<void> {
    const apiKey = await this.question('Enter your Gemini API key: ');
    
    if (this.configManager.validateApiKey(apiKey)) {
      this.configManager.setApiKey(apiKey);
      console.log('✅ API key saved successfully!');
    } else {
      console.log('❌ Invalid API key format. Google API keys should start with "AIzaSy" followed by 33 characters.');
    }
  }

  /**
   * Change the current model
   */
  private async handleChangeModel(): Promise<void> {
    const geminiService = new GeminiService(this.configManager.getConfig().apiKey);
    const models = geminiService.getAvailableModels();
    
    console.log('\nAvailable models:');
    models.forEach((model, index) => {
      console.log(`${index + 1}. ${model}`);
    });
    
    const selection = await this.question('\nEnter model number or name: ');
    let selectedModel: string;
    
    if (/^\d+$/.test(selection)) {
      const index = parseInt(selection) - 1;
      if (index >= 0 && index < models.length) {
        selectedModel = models[index];
      } else {
        console.log('❌ Invalid selection.');
        return;
      }
    } else {
      selectedModel = selection;
    }
    
    this.configManager.setSelectedModel(selectedModel);
    console.log(`✅ Model changed to: ${selectedModel}`);
  }

  /**
   * Show available models
   */
  private async showModels(): Promise<void> {
    const config = this.configManager.getConfig();
    
    if (!config.apiKey) {
      console.log('❌ No API key configured. Please use /setkey first.');
      return;
    }

    const geminiService = new GeminiService(config.apiKey);
    const models = geminiService.getAvailableModels();
    
    console.log('\nAvailable models:');
    models.forEach(model => {
      const info = geminiService.getModelInfo(model);
      if (info) {
        console.log(`\n${info.name} (${model}):`);
        console.log(`  Description: ${info.description}`);
        console.log(`  Capabilities: ${info.capabilities.join(', ')}`);
      } else {
        console.log(`\n${model}`);
      }
    });
  }

  /**
   * Show help
   */
  private showHelp(): void {
    console.log('\nAvailable commands:');
    console.log('  /help     - Show this help message');
    console.log('  /models   - List available models with details');
    console.log('  /setkey   - Set your API key');
    console.log('  /model    - Change the current model');
    console.log('  /quit     - Exit the application');
    console.log('');
  }

  /**
   * Helper function for readline
   */
  private question(prompt: string): Promise<string> {
    return new Promise((resolve) => {
      this.rl.question(prompt, resolve);
    });
  }
}
import * as fs from 'fs';
import * as path from 'path';

interface Config {
  apiKey: string;
  selectedModel: string;
  temperature: number;
  maxTokens: number;
}

export class ConfigManager {
  private configPath: string;
  private config: Config;

  constructor() {
    this.configPath = path.join(process.cwd(), '.env');
    this.config = this.loadConfig();
  }

  /**
   * Load configuration from .env file
   */
  private loadConfig(): Config {
    // Try to read from .env file
    let apiKey = '';
    let selectedModel = 'gemini-1.5-pro-latest';
    let temperature = 0.7;
    let maxTokens = 2048;

    if (fs.existsSync(this.configPath)) {
      const envContent = fs.readFileSync(this.configPath, 'utf8');
      const envLines = envContent.split('\n');

      envLines.forEach(line => {
        const [key, ...valueParts] = line.split('=');
        const value = valueParts.join('=').trim().replace(/['"]/g, '');

        switch (key.trim()) {
          case 'GEMINI_API_KEY':
            apiKey = value;
            break;
          case 'DEFAULT_MODEL':
            selectedModel = value || 'gemini-1.5-pro-latest';
            break;
          case 'TEMPERATURE':
            temperature = parseFloat(value) || 0.7;
            break;
          case 'MAX_TOKENS':
            maxTokens = parseInt(value) || 2048;
            break;
        }
      });
    }

    return {
      apiKey,
      selectedModel,
      temperature,
      maxTokens
    };
  }

  /**
   * Save configuration to .env file
   */
  private saveConfig(): void {
    const envContent = [
      `GEMINI_API_KEY=${this.config.apiKey}`,
      `DEFAULT_MODEL=${this.config.selectedModel}`,
      `TEMPERATURE=${this.config.temperature}`,
      `MAX_TOKENS=${this.config.maxTokens}`
    ].join('\n');

    fs.writeFileSync(this.configPath, envContent, 'utf8');
  }

  /**
   * Get current configuration
   */
  getConfig(): Config {
    return { ...this.config };
  }

  /**
   * Set API key
   */
  setApiKey(apiKey: string): void {
    this.config.apiKey = apiKey;
    this.saveConfig();
  }

  /**
   * Set selected model
   */
  setSelectedModel(model: string): void {
    this.config.selectedModel = model;
    this.saveConfig();
  }

  /**
   * Set temperature
   */
  setTemperature(temp: number): void {
    this.config.temperature = temp;
    this.saveConfig();
  }

  /**
   * Set max tokens
   */
  setMaxTokens(maxTokens: number): void {
    this.config.maxTokens = maxTokens;
    this.saveConfig();
  }

  /**
   * Validate API key format
   */
  validateApiKey(apiKey: string): boolean {
    // Google API keys typically start with "AI" followed by "zaSy" pattern
    // More specifically, they match the pattern: AIzaSy[letters and numbers]
    const apiKeyRegex = /^AIzaSy[a-zA-Z0-9_-]{33}$/;
    return apiKeyRegex.test(apiKey);
  }
}
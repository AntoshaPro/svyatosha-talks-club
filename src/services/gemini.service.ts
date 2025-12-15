import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from '@google/generative-ai';

export class GeminiService {
  private genAI: GoogleGenerativeAI;
  private safetySettings: Array<{ category: HarmCategory; threshold: HarmBlockThreshold }>;

  constructor(apiKey: string) {
    this.genAI = new GoogleGenerativeAI(apiKey);
    this.safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
    ];
  }

  /**
   * Generate text using the specified model
   */
  async generateText(prompt: string, modelName: string = 'gemini-pro'): Promise<string> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: modelName,
        safetySettings: this.safetySettings
      });

      const result = await model.generateContent({
        contents: [{
          role: 'user',
          parts: [{ text: prompt }]
        }],
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 2048,
        }
      });

      const response = await result.response;
      return response.text();
    } catch (error) {
      throw new Error(`Error generating text: ${(error as Error).message}`);
    }
  }

  /**
   * Generate text with chat capabilities
   */
  async generateChatText(history: Array<{role: string, text: string}>, prompt: string, modelName: string = 'gemini-pro'): Promise<string> {
    try {
      const model = this.genAI.getGenerativeModel({ 
        model: modelName,
        safetySettings: this.safetySettings
      });

      const chat = model.startChat({
        history: history.map(msg => ({
          role: msg.role,
          parts: [{ text: msg.text }]
        })),
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 2048,
        }
      });

      const result = await chat.sendMessage(prompt);
      const response = await result.response;
      return response.text();
    } catch (error) {
      throw new Error(`Error generating chat text: ${(error as Error).message}`);
    }
  }

  /**
   * Get available Gemini models
   */
  getAvailableModels(): string[] {
    // Current available Gemini models as of late 2024
    return [
      'gemini-1.5-pro-latest',
      'gemini-1.5-flash-latest',
      'gemini-1.0-pro',  // legacy name for gemini-pro
      'gemini-pro',      // legacy model
      'gemini-pro-vision' // legacy name for gemini-1.0-pro-vision
    ];
  }

  /**
   * Get model information
   */
  getModelInfo(modelName: string): { name: string; description: string; capabilities: string[] } | null {
    const modelsInfo: Record<string, { name: string; description: string; capabilities: string[] }> = {
      'gemini-1.5-pro-latest': {
        name: 'Gemini 1.5 Pro',
        description: 'Mid-size multimodal model that supports text, images, and video.',
        capabilities: ['text', 'images', 'video', 'audio', 'code', 'long context']
      },
      'gemini-1.5-flash-latest': {
        name: 'Gemini 1.5 Flash',
        description: 'Fast and efficient multimodal model for various tasks.',
        capabilities: ['text', 'images', 'video', 'audio', 'code', 'low latency']
      },
      'gemini-1.0-pro': {
        name: 'Gemini 1.0 Pro',
        description: 'Text-based model optimized for language understanding and generation.',
        capabilities: ['text', 'code', 'language tasks']
      },
      'gemini-pro': {
        name: 'Gemini Pro',
        description: 'Legacy name for Gemini 1.0 Pro.',
        capabilities: ['text', 'code', 'language tasks']
      },
      'gemini-pro-vision': {
        name: 'Gemini Pro Vision',
        description: 'Legacy multimodal model supporting text and images.',
        capabilities: ['text', 'images', 'visual understanding']
      }
    };

    return modelsInfo[modelName] || null;
  }
}
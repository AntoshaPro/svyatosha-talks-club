declare module '@google/generative-ai' {
  export enum HarmCategory {
    HARM_CATEGORY_HARASSMENT = "HARM_CATEGORY_HARASSMENT",
    HARM_CATEGORY_HATE_SPEECH = "HARM_CATEGORY_HATE_SPEECH",
    HARM_CATEGORY_SEXUALLY_EXPLICIT = "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    HARM_CATEGORY_DANGEROUS_CONTENT = "HARM_CATEGORY_DANGEROUS_CONTENT"
  }

  export enum HarmBlockThreshold {
    BLOCK_LOW_AND_ABOVE = "BLOCK_LOW_AND_ABOVE",
    BLOCK_MEDIUM_AND_ABOVE = "BLOCK_MEDIUM_AND_ABOVE",
    BLOCK_ONLY_HIGH = "BLOCK_ONLY_HIGH",
    BLOCK_NONE = "BLOCK_NONE"
  }

  export interface GenerationConfig {
    temperature?: number;
    maxOutputTokens?: number;
    topP?: number;
    topK?: number;
  }

  export interface Part {
    text?: string;
    inlineData?: {
      mimeType: string;
      data: string;
    };
  }

  export interface Content {
    role: string;
    parts: Part[];
  }

  export interface RequestOptions {
    timeout?: number;
  }

  export interface GenerateContentRequest {
    contents: Content[];
    generationConfig?: GenerationConfig;
    safetySettings?: Array<{
      category: HarmCategory;
      threshold: HarmBlockThreshold;
    }>;
  }

  export interface GenerateContentResult {
    response: EnhancedGenerateContentResponse;
  }

  export interface EnhancedGenerateContentResponse {
    text: () => string;
    candidates?: Array<any>;
    promptFeedback?: any;
  }

  export interface GenerativeModel {
    generateContent: (request: GenerateContentRequest | string) => Promise<GenerateContentResult>;
    startChat: (config?: {
      history?: Content[];
      generationConfig?: GenerationConfig;
      safetySettings?: Array<{
        category: HarmCategory;
        threshold: HarmBlockThreshold;
      }>;
    }) => GenerativeChat;
  }

  export interface GenerativeChat {
    sendMessage: (message: string | Array<string | Part>) => Promise<GenerateContentResult>;
    getHistory: () => Promise<Content[]>;
  }

  export class GoogleGenerativeAI {
    constructor(apiKey: string);
    getGenerativeModel(params: {
      model: string;
      safetySettings?: Array<{
        category: HarmCategory;
        threshold: HarmBlockThreshold;
      }>;
    }): GenerativeModel;
  }
}
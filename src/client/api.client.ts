import axios from 'axios';

// Define types for axios instead of importing them
type AxiosInstance = any;
type AxiosResponse<T = any> = {
  data: T;
  status: number;
  statusText: string;
  headers: any;
  config: any;
};

export interface ChatRequest {
  message: string;
  model?: string;
}

export interface ChatResponse {
  response: string;
  model: string;
  timestamp: string;
}

export interface ModelInfo {
  name: string;
  description: string;
  capabilities: string[];
}

export class ApiClient {
  private client: AxiosInstance;

  constructor(baseURL: string, apiKey?: string) {
    this.client = axios.create({
      baseURL,
      headers: {
        'Content-Type': 'application/json',
        ...(apiKey && { 'x-api-key': apiKey })
      }
    });
  }

  /**
   * Get available models
   */
  async getModels(apiKey: string): Promise<string[]> {
    try {
      const response: AxiosResponse<{ models: string[] }> = await this.client.get('/api/models', {
        headers: { 'x-api-key': apiKey }
      });
      return response.data.models;
    } catch (error) {
      throw new Error(`Failed to fetch models: ${(error as Error).message}`);
    }
  }

  /**
   * Send a chat message
   */
  async chat(request: ChatRequest, apiKey: string): Promise<ChatResponse> {
    try {
      const response: AxiosResponse<ChatResponse> = await this.client.post('/api/chat', request, {
        headers: { 'x-api-key': apiKey }
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get response: ${(error as Error).message}`);
    }
  }

  /**
   * Update API key in config
   */
  async updateApiKey(newApiKey: string): Promise<void> {
    try {
      await this.client.post('/api/config/api-key', { apiKey: newApiKey });
    } catch (error) {
      throw new Error(`Failed to update API key: ${(error as Error).message}`);
    }
  }

  /**
   * Get current configuration
   */
  async getConfig(): Promise<any> {
    try {
      const response: AxiosResponse<any> = await this.client.get('/api/config');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get config: ${(error as Error).message}`);
    }
  }
}
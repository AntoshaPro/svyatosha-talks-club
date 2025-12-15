import express, { Request, Response } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { GeminiService } from './services/gemini.service';
import { ConfigManager } from './config/config.manager';

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Initialize config manager
const configManager = new ConfigManager();

// Routes
app.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Gemini API Client Server Running' });
});

// Get available models
app.get('/api/models', (req: Request, res: Response) => {
  try {
    const apiKey = req.headers['x-api-key'] as string;
    if (!apiKey) {
      return res.status(401).json({ error: 'API Key is required' });
    }

    const geminiService = new GeminiService(apiKey);
    const models = geminiService.getAvailableModels();
    res.json({ models });
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
  return; // Explicitly return to satisfy TS compiler
});

// Chat endpoint
app.post('/api/chat', async (req: Request, res: Response) => {
  try {
    const { message, model = 'gemini-pro' } = req.body;
    const apiKey = req.headers['x-api-key'] as string;

    if (!apiKey) {
      return res.status(401).json({ error: 'API Key is required' });
    }

    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    const geminiService = new GeminiService(apiKey);
    const response = await geminiService.generateText(message, model);
    
    res.json({ 
      response,
      model,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
  return; // Explicitly return to satisfy TS compiler
});

// Set API key
app.post('/api/config/api-key', (req: Request, res: Response) => {
  try {
    const { apiKey } = req.body;
    
    if (!apiKey) {
      return res.status(400).json({ error: 'API Key is required' });
    }

    configManager.setApiKey(apiKey);
    res.json({ success: true, message: 'API Key updated successfully' });
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
  return; // Explicitly return to satisfy TS compiler
});

// Get current configuration
app.get('/api/config', (req: Request, res: Response) => {
  try {
    const config = configManager.getConfig();
    res.json(config);
  } catch (error) {
    res.status(500).json({ error: (error as Error).message });
  }
  return; // Explicitly return to satisfy TS compiler
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
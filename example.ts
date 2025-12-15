/**
 * Example usage of the Gemini API Client
 * This demonstrates how to use the API client to interact with Gemini models
 */

import { ApiClient } from './src/client/api.client';

async function example() {
  // Initialize the API client
  const client = new ApiClient('http://localhost:3000'); // Adjust the URL as needed
  
  // Replace with your actual API key
  const API_KEY = 'YOUR_GEMINI_API_KEY_HERE';
  
  try {
    // Get available models
    console.log('Fetching available models...');
    const models = await client.getModels(API_KEY);
    console.log('Available models:', models);
    
    // Send a chat message
    console.log('\nSending a chat message...');
    const chatResponse = await client.chat({
      message: 'Hello, how are you?',
      model: 'gemini-1.5-flash-latest'
    }, API_KEY);
    
    console.log('Response:', chatResponse.response);
    console.log('Model used:', chatResponse.model);
    
    // Get current configuration
    console.log('\nFetching configuration...');
    const config = await client.getConfig();
    console.log('Current config:', config);
    
  } catch (error) {
    console.error('Error:', error);
  }
}

// Run the example
example();
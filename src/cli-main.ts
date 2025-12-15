#!/usr/bin/env node

import { CliInterface } from './cli/cli.interface';

async function main(): Promise<void> {
  try {
    const cli = new CliInterface();
    await cli.start();
  } catch (error) {
    console.error('Application error:', error);
    process.exit(1);
  }
}

// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
  process.exit(1);
});

process.on('unhandledRejection', (reason) => {
  console.error('Unhandled Rejection:', reason);
  process.exit(1);
});

main();
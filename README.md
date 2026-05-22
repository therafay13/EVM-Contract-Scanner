# EVM Contract Scanner (Lite)

A lightweight, regex-based static analysis tool for quickly spotting common vulnerabilities in Solidity smart contracts.
Created by CanuteTheWise.

## Features
- Detects missing `pragma` versions.
- Highlights `tx.origin` usage (Phishing vulnerabilities).
- Flags `block.timestamp` usage (Weak randomness).
- Warns about `selfdestruct`.

## Usage
```bash
python scanner.py <path_to_contract.sol>
```

*Disclaimer: This is a preliminary tool and should not replace comprehensive manual auditing.*

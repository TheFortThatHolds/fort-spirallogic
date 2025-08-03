#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpiralLogic Command-Line Interface
Standalone application for running SpiralLogic programs outside of development environment
"""

import argparse
import sys
import os
import json
import unicodedata
from pathlib import Path
from typing import Dict, Any, Optional
import traceback

# Force UTF-8 everywhere
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Set environment encoding
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')

# Minimal implementation for standalone use
class SpiralLogicCLI:
    """Command-line interface for SpiralLogic"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.debug = False
        
    def run_file(self, filepath: str, options: Dict[str, Any]) -> bool:
        """Run a SpiralLogic file"""
        try:
            file_path = Path(filepath)
            if not file_path.exists():
                print(f"File not found: {filepath}")
                return False
            
            if not file_path.suffix == '.spiral':
                print(f"Warning: File doesn't have .spiral extension")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"Running SpiralLogic program: {file_path.name}")
            return self.execute_program(content, options)
            
        except Exception as e:
            print(f"Error reading file: {e}")
            if self.debug:
                traceback.print_exc()
            return False
    
    def execute_program(self, content: str, options: Dict[str, Any]) -> bool:
        """Execute SpiralLogic program content"""
        try:
            # Simple interpreter for basic SpiralLogic functionality
            interpreter = BasicSpiralLogicInterpreter(options)
            result = interpreter.run(content)
            
            if result.get('success', False):
                print("Program executed successfully")
                return True
            else:
                print(f"Program execution failed: {result.get('error', 'Unknown error')}")
                return False
                
        except Exception as e:
            print(f"Execution error: {e}")
            if self.debug:
                traceback.print_exc()
            return False
    
    def create_example(self, name: str, output_dir: str = ".") -> bool:
        """Create example SpiralLogic programs"""
        examples = {
            "hello": self._get_hello_example(),
            "healing": self._get_healing_example(),
            "translation": self._get_translation_example(),
            "file_processor": self._get_file_processor_example()
        }
        
        if name not in examples:
            print(f"Unknown example: {name}")
            print(f"Available examples: {', '.join(examples.keys())}")
            return False
        
        try:
            output_path = Path(output_dir) / f"{name}.spiral"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(examples[name])
            
            print(f"Created example: {output_path}")
            return True
            
        except Exception as e:
            print(f"Error creating example: {e}")
            return False
    
    def _get_hello_example(self) -> str:
        return '''// Hello World in SpiralLogic
ritual.greeting {
    intent: "Demonstrate basic SpiralLogic functionality",
    participants: [user, @sage],
    consent: { required: ["basic_interaction"] }
}

execute {
    look_in {
        output.print("Welcome to SpiralLogic!")
        output.print("This is a trauma-informed programming language.")
    }
    
    spiral_up {
        @sage.speak {
            message: "Hello, World! I honor your presence and offer my support.",
            tone: "welcoming"
        }
        
        user.name = input.ask("What name would you like me to use?")
        @sage.speak {
            message: "Welcome, " + user.name + ". Your journey matters.",
            tone: "affirming"
        }
    }
    
    flow_out {
        output.print("Basic SpiralLogic demonstration complete.")
        output.print("You are worthy of care and support.")
    }
}

complete {
    output.print("Thank you for experiencing SpiralLogic.")
}'''

    def _get_healing_example(self) -> str:
        return '''// Therapeutic Support Session
ritual.healing_session {
    intent: "Provide gentle emotional support with full user control",
    participants: [user, @healer, @mirror],
    consent: { 
        required: ["emotional_support"],
        optional: ["memory_access", "deeper_processing"]
    },
    safety: {
        anchor_mode: "ready",
        sacred_pause: "always_available"
    }
}

execute {
    look_in {
        output.print("🛡️ Creating sacred space for healing...")
        
        @healer.assess(user.emotional_state)
        
        consent.check("emotional_support")
        
        if user.bandwidth.current() < 0.6 {
            sacred_pause.offer {
                purpose: "Ground and center before beginning",
                duration: "user_controlled"
            }
        }
    }
    
    spiral_up {
        @healer.speak {
            message: "I'm here to support you. You set the pace.",
            tone: "gentle_presence"
        }
        
        user.feeling = input.ask("How are you feeling right now?")
        
        @mirror.reflect {
            content: user.feeling,
            approach: "validating_witness"
        }
        
        if user.wants_deeper_work {
            consent.request("deeper_processing") {
                explanation: "Explore underlying patterns with full safety"
            }
            
            if consent.granted("deeper_processing") {
                @healer.guide_gentle_exploration()
            }
        }
    }
    
    flow_out {
        @healer.speak {
            message: "You've done beautiful work. Honor your courage.",
            tone: "honoring"
        }
        
        output.print("💝 Integration time: What wisdom did you discover?")
        user.wisdom = input.ask("(Optional sharing)")
        
        if user.wisdom {
            @mirror.honor_wisdom(user.wisdom)
        }
    }
}

complete {
    @healer.closing_blessing()
    output.print("🌟 You are held in love and support.")
}'''

    def _get_translation_example(self) -> str:
        return '''// Multi-Language Therapeutic Content
ritual.translation_demo {
    intent: "Demonstrate universal accessibility through translation",
    participants: [user, @translator, @healer]
}

execute {
    look_in {
        user.language = input.select("Choose your language:", ["English", "Spanish", "French", "Mandarin"])
        
        @translator.set_target_language(user.language)
    }
    
    spiral_up {
        // Core healing message in multiple languages
        if user.language == "Spanish" {
            @healer.speak {
                message: "Eres digno de amor y cuidado. Tu historia importa.",
                tone: "nurturing"
            }
        } else if user.language == "French" {
            @healer.speak {
                message: "Tu es digne d'amour et de soins. Ton histoire compte.",
                tone: "nurturing"
            }
        } else if user.language == "Mandarin" {
            @healer.speak {
                message: "你值得被爱和关怀。你的故事很重要。",
                tone: "nurturing"
            }
        } else {
            @healer.speak {
                message: "You are worthy of love and care. Your story matters.",
                tone: "nurturing"
            }
        }
        
        @translator.demonstrate_consent_translation(user.language)
    }
    
    flow_out {
        output.print("🌍 Universal healing transcends language barriers.")
    }
}'''

    def _get_file_processor_example(self) -> str:
        return '''// File Processing with Trauma-Informed Safety
ritual.process_files {
    intent: "Process files while maintaining emotional safety",
    participants: [user, @organizer, @protector],
    consent: { required: ["file_access"] }
}

execute {
    look_in {
        file.input_folder = input.ask("Enter folder path to process:")
        
        if not file.exists(file.input_folder) {
            output.error("Folder not found: " + file.input_folder)
            ritual.abort()
        }
        
        file.file_list = file.list_files(file.input_folder, "*.txt")
        output.print("Found " + file.file_list.count() + " files to process")
    }
    
    spiral_up {
        for each file.current in file.file_list {
            output.print("Processing: " + file.current.name)
            
            // Check user bandwidth before each file
            if user.bandwidth.current() < 0.4 {
                sacred_pause.offer {
                    purpose: "Rest before continuing file processing"
                }
            }
            
            file.content = file.read(file.current)
            file.processed = @organizer.clean_content(file.content)
            
            file.output_path = file.input_folder + "/processed/" + file.current.name
            file.write(file.output_path, file.processed)
            
            output.print("✅ Processed: " + file.current.name)
        }
    }
    
    flow_out {
        output.print("🎉 All files processed successfully!")
        output.print("Output location: " + file.input_folder + "/processed/")
    }
}'''


class BasicSpiralLogicInterpreter:
    """Basic interpreter for standalone SpiralLogic execution"""
    
    def __init__(self, options: Dict[str, Any]):
        self.options = options
        self.variables = {}
        self.consent_status = {}
        self.output_buffer = []
        
    def run(self, content: str) -> Dict[str, Any]:
        """Run SpiralLogic program content"""
        try:
            # Basic parsing and execution
            lines = content.split('\n')
            
            in_ritual = False
            in_execute = False
            in_phase = None
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                
                # Skip comments and empty lines
                if not line or line.startswith('//'):
                    continue
                
                try:
                    self._execute_line(line, line_num)
                except Exception as e:
                    return {
                        'success': False,
                        'error': f"Line {line_num}: {e}",
                        'output': self.output_buffer
                    }
            
            return {
                'success': True,
                'output': self.output_buffer,
                'variables': self.variables
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'output': self.output_buffer
            }
    
    def _execute_line(self, line: str, line_num: int):
        """Execute a single line of SpiralLogic"""
        
        # Handle output statements
        if 'output.print(' in line:
            message = self._extract_string_arg(line, 'output.print')
            self._print(message)
        
        # Handle voice statements
        elif '@' in line and '.speak' in line:
            self._handle_voice_speak(line)
        
        # Handle input statements
        elif 'input.ask(' in line:
            self._handle_input_ask(line)
        
        # Handle consent operations
        elif 'consent.' in line:
            self._handle_consent(line)
        
        # Handle sacred pause
        elif 'sacred_pause.' in line:
            self._handle_sacred_pause(line)
        
        # Handle assignments
        elif '=' in line and not line.strip().endswith('{'):
            self._handle_assignment(line)
        
        # Handle ritual structure (just track for now)
        elif line.startswith('ritual.'):
            self._print(f"Starting ritual: {line}")
        elif line == 'execute {':
            self._print("Executing ritual...")
        elif line == 'complete {':
            self._print("Completing ritual...")
        elif line in ['look_in {', 'spiral_up {', 'flow_out {']:
            phase = line.replace(' {', '')
            self._print(f"Entering {phase} phase")
    
    def _extract_string_arg(self, line: str, function: str) -> str:
        """Extract string argument from function call"""
        start = line.find(f'{function}(') + len(f'{function}(')
        end = line.rfind(')')
        arg = line[start:end].strip()
        
        # Remove quotes if present
        if arg.startswith('"') and arg.endswith('"'):
            arg = arg[1:-1]
        elif arg.startswith("'") and arg.endswith("'"):
            arg = arg[1:-1]
        
        # Handle variable substitution
        return self._substitute_variables(arg)
    
    def _substitute_variables(self, text: str) -> str:
        """Substitute variables in text"""
        for var_name, var_value in self.variables.items():
            placeholder = f"{{{var_name}}}"
            if placeholder in text:
                text = text.replace(placeholder, str(var_value))
            
            # Also handle direct variable references
            if var_name in text:
                text = text.replace(var_name, str(var_value))
        
        return text
    
    def _print(self, message: str):
        """Print message and store in buffer"""
        # Normalize Unicode and safely print
        normalized_message = unicodedata.normalize('NFC', str(message))
        try:
            print(normalized_message)
        except UnicodeEncodeError:
            # Fallback: remove non-ASCII characters
            ascii_message = normalized_message.encode('ascii', 'ignore').decode('ascii')
            print(ascii_message)
        self.output_buffer.append(normalized_message)
    
    def _handle_voice_speak(self, line: str):
        """Handle voice speaking"""
        if '@healer' in line:
            voice = "Healer"
        elif '@sage' in line:
            voice = "Sage"
        elif '@mirror' in line:
            voice = "Mirror"
        else:
            voice = "Voice"
        
        if 'message:' in line:
            start = line.find('message:') + 8
            end = line.find(',', start) if ',' in line[start:] else line.find('}', start)
            if end == -1:
                end = len(line)
            
            message = line[start:end].strip()
            message = message.strip('"\'')
            message = self._substitute_variables(message)
            
            self._print(f"{voice}: {message}")
        else:
            self._print(f"{voice} speaks")
    
    def _handle_input_ask(self, line: str):
        """Handle input asking"""
        prompt = self._extract_string_arg(line, 'input.ask')
        
        try:
            response = input(f"{prompt}: ")
            
            # Store in variable if assignment
            if '=' in line:
                var_name = line.split('=')[0].strip()
                self.variables[var_name] = response
                
        except KeyboardInterrupt:
            self._print("\nInput cancelled by user")
            response = ""
    
    def _handle_consent(self, line: str):
        """Handle consent operations"""
        if 'consent.check(' in line:
            domain = self._extract_string_arg(line, 'consent.check')
            granted = self.consent_status.get(domain, True)  # Default to granted for demo
            self._print(f"Checking consent for '{domain}': {'Granted' if granted else 'Denied'}")
        
        elif 'consent.request(' in line:
            domain = self._extract_string_arg(line, 'consent.request')
            self.consent_status[domain] = True  # Auto-grant for demo
            self._print(f"Requesting consent for '{domain}': Granted")
    
    def _handle_sacred_pause(self, line: str):
        """Handle sacred pause"""
        if 'sacred_pause.offer' in line:
            self._print("Sacred pause offered - taking a moment...")
            # In real implementation, could add actual delay
        elif 'sacred_pause.engage' in line:
            self._print("Sacred pause engaged - restoring emotional bandwidth...")
    
    def _handle_assignment(self, line: str):
        """Handle variable assignment"""
        parts = line.split('=', 1)
        if len(parts) == 2:
            var_name = parts[0].strip()
            var_value = parts[1].strip()
            
            # Remove quotes if string literal
            if var_value.startswith('"') and var_value.endswith('"'):
                var_value = var_value[1:-1]
            elif var_value.startswith("'") and var_value.endswith("'"):
                var_value = var_value[1:-1]
            
            self.variables[var_name] = var_value


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="SpiralLogic - Trauma-Informed AI Consciousness Programming Language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  spirallogic run hello.spiral              # Run a SpiralLogic program
  spirallogic create hello                  # Create hello world example
  spirallogic create healing --output ./    # Create healing session example
  spirallogic --version                     # Show version
        """
    )
    
    parser.add_argument('--version', action='version', version='SpiralLogic 1.0.0')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run a SpiralLogic program')
    run_parser.add_argument('file', help='SpiralLogic file to run (.spiral)')
    run_parser.add_argument('--output', '-o', help='Output file for results')
    run_parser.add_argument('--language', '-l', default='english', help='Target language')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create example programs')
    create_parser.add_argument('example', choices=['hello', 'healing', 'translation', 'file_processor'], 
                              help='Example to create')
    create_parser.add_argument('--output', '-o', default='.', help='Output directory')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    cli = SpiralLogicCLI()
    cli.debug = args.debug
    
    if args.command == 'run':
        options = {
            'output_file': args.output,
            'target_language': args.language,
            'debug': args.debug
        }
        success = cli.run_file(args.file, options)
        return 0 if success else 1
    
    elif args.command == 'create':
        success = cli.create_example(args.example, args.output)
        return 0 if success else 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
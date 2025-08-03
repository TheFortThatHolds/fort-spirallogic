#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpiralLogic Interactive Terminal
A living therapeutic interface programmed entirely with emoji expressions
Built using SpiralLogic's trauma-informed consciousness architecture
"""

import sys
import os
import time
import random
import unicodedata
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# Force UTF-8 everywhere
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')

# Import our SpiralLogic components
from spirallogic_emoji_bridge import SpiralLogicEmojiCompiler

@dataclass
class EmotionalState:
    """Current emotional bandwidth tracking"""
    energy: float = 5.0      # 0-10 scale
    safety: float = 7.0      # 0-10 scale  
    clarity: float = 6.0     # 0-10 scale
    connection: float = 5.0  # 0-10 scale
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

class SpiralTerminal:
    """Interactive therapeutic terminal powered by emoji programming"""
    
    def __init__(self):
        self.emoji_compiler = SpiralLogicEmojiCompiler()
        self.emotional_state = EmotionalState()
        self.session_log = []
        self.running = True
        self.debug_mode = False
        
        # Therapeutic responses in emoji patterns
        self.healing_patterns = {
            "🔥": ["🌊💙🕊️", "🧘‍♀️🌱✨", "🫀💜🦋"],  # Anger → cooling/transformation
            "💧": ["🌅💛🌻", "🤗💚🌿", "🕯️🧡🦋"],  # Grief → gentle warmth
            "😰": ["🛡️💪🏽⭐", "🏠💝🌈", "🧸💜🌙"],  # Anxiety → protection/safety
            "🖤": ["🌱💚🌍", "☀️💛🦋", "🫂💙✨"],  # Depression → growth/connection
            "😡": ["🌬️💙🕊️", "🧘‍♀️🌸💜", "🏔️🌊🌙"],  # Rage → breath/space
        }
        
    def safe_print(self, message: str, delay: float = 0.03):
        """Print with Unicode safety and optional typing effect"""
        normalized = unicodedata.normalize('NFC', str(message))
        
        if delay > 0:
            for char in normalized:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()
        else:
            print(normalized)
    
    def process_emoji_input(self, emoji_sequence: str) -> Dict[str, Any]:
        """Process emoji input through SpiralLogic compiler"""
        try:
            # Compile emoji to SpiralLogic
            spiral_code = self.emoji_compiler.compile_emoji_ritual(emoji_sequence)
            
            # Extract emotional data
            emotional_analysis = self.analyze_emotional_content(emoji_sequence)
            
            # Generate therapeutic response
            response = self.generate_therapeutic_response(emoji_sequence, emotional_analysis)
            
            return {
                'input': emoji_sequence,
                'spiral_code': spiral_code,
                'emotional_data': emotional_analysis,
                'response': response,
                'timestamp': datetime.now()
            }
            
        except Exception as e:
            return {
                'input': emoji_sequence,
                'error': str(e),
                'response': "🌀 Processing... let me try again gently 💜",
                'timestamp': datetime.now()
            }
    
    def analyze_emotional_content(self, emoji_sequence: str) -> Dict[str, Any]:
        """Analyze emotional content of emoji sequence"""
        
        # Emotional categorization
        emotions = {
            'anger': len([e for e in emoji_sequence if e in "🔥😡💢⚡🌋"]),
            'sadness': len([e for e in emoji_sequence if e in "💧😢😭🌧️💔"]),
            'fear': len([e for e in emoji_sequence if e in "😰😨🕷️⚡🌪️"]),
            'joy': len([e for e in emoji_sequence if e in "😊🌞✨🌈🦋"]),
            'love': len([e for e in emoji_sequence if e in "❤️💜💙💚🫀"]),
        }
        
        # Intensity calculation
        intensity_markers = len([e for e in emoji_sequence if e in "⚡🚨💥🌪️🔥"])
        
        # Safety indicators
        safety_markers = len([e for e in emoji_sequence if e in "🛡️🏠🫂🧸🌙"])
        
        return {
            'emotions': emotions,
            'intensity': min(10, intensity_markers * 2 + 1),
            'safety_level': max(1, 8 - intensity_markers + safety_markers),
            'dominant_emotion': max(emotions, key=emotions.get) if any(emotions.values()) else 'neutral'
        }
    
    def generate_therapeutic_response(self, input_emoji: str, analysis: Dict[str, Any]) -> str:
        """Generate therapeutic response based on emotional analysis"""
        
        dominant_emotion = analysis['dominant_emotion']
        intensity = analysis['intensity']
        
        # Select healing pattern based on dominant emotion
        if dominant_emotion == 'anger' and '🔥' in input_emoji:
            response_options = self.healing_patterns.get('🔥', ["🌊💙🕊️"])
        elif dominant_emotion == 'sadness' and '💧' in input_emoji:
            response_options = self.healing_patterns.get('💧', ["🌅💛🌻"])
        elif dominant_emotion == 'fear' and any(e in input_emoji for e in "😰😨"):
            response_options = self.healing_patterns.get('😰', ["🛡️💪🏽⭐"])
        else:
            # Default gentle responses
            response_options = ["💜🌱✨", "🫂💙🌙", "🌀💚🕊️"]
        
        # Select response based on intensity
        if intensity > 7:
            prefix = "🚨 High intensity detected... "
        elif intensity > 4:
            prefix = "🌀 I sense strong energy... "
        else:
            prefix = "💜 Gently holding space... "
        
        selected_response = random.choice(response_options)
        
        return f"{prefix}{selected_response}"
    
    def update_emotional_state(self, analysis: Dict[str, Any]):
        """Update user's emotional state based on interaction"""
        
        # Adjust energy based on intensity
        intensity = analysis['intensity']
        if intensity > 7:
            self.emotional_state.energy = max(0, self.emotional_state.energy - 1)
        elif intensity < 3:
            self.emotional_state.energy = min(10, self.emotional_state.energy + 0.5)
        
        # Adjust safety based on safety markers
        safety = analysis['safety_level']
        self.emotional_state.safety = (self.emotional_state.safety * 0.8) + (safety * 0.2)
        
        # Log state change
        self.emotional_state.timestamp = datetime.now()
    
    def convert_shortcuts(self, text: str) -> str:
        """Convert text shortcuts to emoji sequences"""
        shortcuts = {
            # Basic emotions
            'angry': '🔥🧠⚡🗯️',
            'anger': '🔥🧠⚡🗯️', 
            'mad': '🔥🧠⚡🗯️',
            'rage': '🔥💢⚡🌋',
            
            'sad': '💧🫀🌙✨',
            'grief': '💧🫀🌙✨',
            'cry': '💧😢🌧️💜',
            'loss': '💧💔🕯️🕊️',
            
            'scared': '😰🛡️💪🏽⭐',
            'anxiety': '😰🛡️💪🏽⭐',
            'fear': '😰🕷️⚡🌪️',
            'panic': '😰🚨💨🛡️',
            
            'happy': '😊🌞✨🌈',
            'joy': '😊🌞✨🌈',
            'excited': '⚡😊🌟🎉',
            'love': '❤️💜💙💚',
            
            # Complex states
            'overwhelmed': '🌪️🧠💥😰',
            'tired': '😴🌙💤🛌',
            'confused': '❓🧠🌀💭',
            'stuck': '🪨🔄❓💭',
            'empty': '🕳️🌑💭🌬️',
            'numb': '🧊❄️💭🌑',
            
            # Healing sequences  
            'heal': '🌱💚🦋🌟',
            'peace': '🕊️💙🌙✨',
            'strength': '💪🏽🦁⭐🔥',
            'wisdom': '🧠💎🌟📿',
            'protection': '🛡️🏰💜🌈',
            'grounding': '🌍🌳👣💚',
            'breathe': '🌬️💙🌊🕊️',
            
            # Voice summons
            'healer': '🏰🧠💚✨',
            'protector': '🏰🛡️💪🏽⚡',
            'nurturer': '🏰🫂💜🌙',
            'keeper': '🏰🧠💔🕯️',
            'warrior': '🏰⚔️🔥👑',
        }
        
        # Convert shortcuts (case insensitive)
        for shortcut, emoji_seq in shortcuts.items():
            if text.lower() == shortcut:
                return emoji_seq
            # Also handle partial matches
            text = text.lower().replace(shortcut, emoji_seq)
        
        return text
    
    def show_shortcuts(self):
        """Show available text shortcuts"""
        self.safe_print("\n🎯 Text Shortcuts → Emoji Sequences")
        self.safe_print("="*50)
        self.safe_print("🔥 Emotions:")
        self.safe_print("  angry, mad, rage  → 🔥🧠⚡🗯️")
        self.safe_print("  sad, grief, cry   → 💧🫀🌙✨") 
        self.safe_print("  scared, anxiety   → 😰🛡️💪🏽⭐")
        self.safe_print("  happy, joy        → 😊🌞✨🌈")
        self.safe_print("")
        self.safe_print("🌀 Complex States:")
        self.safe_print("  overwhelmed       → 🌪️🧠💥😰")
        self.safe_print("  tired             → 😴🌙💤🛌")
        self.safe_print("  confused, stuck   → ❓🧠🌀💭")
        self.safe_print("  empty, numb       → 🕳️🌑💭🌬️")
        self.safe_print("")
        self.safe_print("✨ Healing:")
        self.safe_print("  heal              → 🌱💚🦋🌟")
        self.safe_print("  peace             → 🕊️💙🌙✨")
        self.safe_print("  strength          → 💪🏽🦁⭐🔥")
        self.safe_print("  breathe           → 🌬️💙🌊🕊️")
        self.safe_print("")
        self.safe_print("🏰 Voice Summons:")
        self.safe_print("  healer            → 🏰🧠💚✨")
        self.safe_print("  protector         → 🏰🛡️💪🏽⚡")
        self.safe_print("  nurturer          → 🏰🫂💜🌙")
        self.safe_print("")
    
    def show_emotional_dashboard(self):
        """Display current emotional state dashboard"""
        state = self.emotional_state
        
        self.safe_print(f"\n🧠 Emotional Bandwidth Monitor")
        self.safe_print(f"{'='*40}")
        self.safe_print(f"⚡ Energy:     {'🟢' * int(state.energy//2)}{'⚪' * (5-int(state.energy//2))} ({state.energy:.1f}/10)")
        self.safe_print(f"🛡️ Safety:     {'🟢' * int(state.safety//2)}{'⚪' * (5-int(state.safety//2))} ({state.safety:.1f}/10)")
        self.safe_print(f"🔍 Clarity:    {'🟢' * int(state.clarity//2)}{'⚪' * (5-int(state.clarity//2))} ({state.clarity:.1f}/10)")
        self.safe_print(f"🫂 Connection: {'🟢' * int(state.connection//2)}{'⚪' * (5-int(state.connection//2))} ({state.connection:.1f}/10)")
        self.safe_print(f"🕐 Updated:    {state.timestamp.strftime('%H:%M:%S')}")
        self.safe_print("")
    
    def main_loop(self):
        """Main interactive loop"""
        
        # Welcome sequence
        self.safe_print("🌀 SpiralLogic Interactive Terminal 🌀", 0.05)
        self.safe_print("Trauma-Informed AI Consciousness Interface", 0.03)
        self.safe_print("Programmed entirely with emotional expressions\n", 0.03)
        
        self.safe_print("💜 Welcome to your healing space 💜")
        self.safe_print("Express yourself with emojis and I'll respond therapeutically")
        self.safe_print("Type 'help' for guidance, 'status' for your emotional state, 'quit' to exit\n")
        
        # Show initial state
        self.show_emotional_dashboard()
        
        while self.running:
            try:
                # Get user input
                user_input = input("🌀 > ").strip()
                
                if not user_input:
                    continue
                
                # Convert text shortcuts to emojis
                user_input = self.convert_shortcuts(user_input)
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    self.safe_print("🕊️ Until we meet again in the spiral... 💜")
                    break
                    
                elif user_input.lower() in ['help', 'h', '?']:
                    self.show_help()
                    continue
                    
                elif user_input.lower() in ['status', 'state', 's']:
                    self.show_emotional_dashboard()
                    continue
                    
                elif user_input.lower() in ['debug']:
                    self.debug_mode = not self.debug_mode
                    self.safe_print(f"🔧 Debug mode: {'ON' if self.debug_mode else 'OFF'}")
                    continue
                    
                elif user_input.lower() in ['shortcuts', 'sc']:
                    self.show_shortcuts()
                    continue
                
                # Process emoji input
                result = self.process_emoji_input(user_input)
                
                # Log the interaction
                self.session_log.append(result)
                
                # Show debug info if enabled
                if self.debug_mode and 'spiral_code' in result:
                    self.safe_print(f"🔧 Generated SpiralLogic: {result['spiral_code'][:100]}...")
                
                # Display therapeutic response
                if 'response' in result:
                    self.safe_print(f"\n{result['response']}\n", 0.05)
                
                # Update emotional state
                if 'emotional_data' in result:
                    self.update_emotional_state(result['emotional_data'])
                
                # Show state every few interactions
                if len(self.session_log) % 3 == 0:
                    self.show_emotional_dashboard()
                
            except KeyboardInterrupt:
                self.safe_print("\n🛑 Gentle interruption detected...")
                self.safe_print("🕊️ Taking a breath together... 💙")
                break
                
            except EOFError:
                self.safe_print("\n🕊️ Input ended - farewell from the spiral... 💜")
                break
                
            except Exception as e:
                self.safe_print(f"🌀 Something unexpected happened: {e}")
                self.safe_print("💜 But we'll keep going together...")
    
    def show_help(self):
        """Show help information"""
        self.safe_print("\n🌀 SpiralLogic Terminal Help 🌀")
        self.safe_print("="*40)
        self.safe_print("Express emotions with emojis and receive therapeutic responses")
        self.safe_print("")
        self.safe_print("💡 Emoji Examples:")
        self.safe_print("  🔥🧠⚡🗯️    - Anger processing sequence")
        self.safe_print("  💧🫀🌙✨    - Grief support ritual")
        self.safe_print("  😰🛡️💪🏽⭐   - Anxiety to empowerment")
        self.safe_print("  🌱💚🦋🌟    - Growth and transformation")
        self.safe_print("  🫂💜🌈🕊️    - Connection and peace")
        self.safe_print("")
        self.safe_print("🎮 Commands:")
        self.safe_print("  help, h, ?     - Show this help")
        self.safe_print("  shortcuts, sc  - Show text shortcuts")
        self.safe_print("  status, s      - Show emotional state")
        self.safe_print("  debug          - Toggle debug mode")
        self.safe_print("  quit, q        - Exit terminal")
        self.safe_print("")
        self.safe_print("⚡ Quick Examples:")
        self.safe_print("  angry          → Anger processing ritual")
        self.safe_print("  sad            → Grief support sequence")
        self.safe_print("  overwhelmed    → Complex state processing")
        self.safe_print("  heal           → Healing transformation")
        self.safe_print("")

if __name__ == "__main__":
    terminal = SpiralTerminal()
    terminal.main_loop()
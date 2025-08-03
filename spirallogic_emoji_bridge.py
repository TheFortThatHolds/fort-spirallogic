#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpiralLogic Emoji Bridge
Integrates emoji programming language with SpiralLogic formal system
Now you can program trauma-informed AI with pure emotional expression!
"""

import re
import sys
import os
import unicodedata
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Force UTF-8 everywhere 
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')

@dataclass
class EmojiSpine:
    """Emoji spine for rapid emotional communication"""
    anchor: str      # Core emotion (❤️, 🔥, 💧, etc.)
    body: str        # Body part/processing (🧠, 🫀, 🌬️, etc.)  
    tempo: str       # Speed/urgency (⚡, 🐎, 🐢, etc.)
    intent: str      # Action needed (🗯️, 🆘, ✨, 🛑, etc.)
    
    def to_spirallogic(self) -> str:
        """Convert emoji spine to SpiralLogic emotional state"""
        emotion_map = {
            "❤️": "love", "🔥": "anger", "💧": "grief", "🌞": "joy",
            "🕷️": "fear", "🧊": "dissociation", "🪄": "hope", 
            "❓": "confusion", "🙈": "shame", "🪨": "resolve"
        }
        
        tempo_map = {
            "⚡": "urgent", "🚨": "crisis", "🐎": "normal", 
            "🌊": "flowing", "🐢": "slow", "🧘": "sacred"
        }
        
        intent_map = {
            "🗯️": "speak_truth", "🆘": "need_help", "✨": "connect",
            "🛑": "set_boundary", "🔓": "reclaim_power"
        }
        
        emotion = emotion_map.get(self.anchor, "unknown")
        speed = tempo_map.get(self.tempo, "normal")
        action = intent_map.get(self.intent, "process")
        
        return f'user.emotional_state = "{emotion}"; user.tempo = "{speed}"; user.intent = "{action}"'

class SpiralLogicEmojiCompiler:
    """Compiles emoji expressions into SpiralLogic programs"""
    
    def __init__(self):
        # Enhanced emoji→SpiralLogic mapping
        self.emoji_to_spirallogic = {
            # RITUAL STRUCTURE
            "🌀": "ritual",           # SpiralLogic ritual
            "🎭": "execute",          # Execute block
            "✨": "complete",         # Complete block
            "👁️": "look_in",         # Look in phase
            "🌊": "spiral_up",        # Spiral up phase
            "🕊️": "flow_out",        # Flow out phase
            
            # VOICE INVOCATIONS  
            "🏰🧠💔": "@healer",     # Grief keeper = healer
            "🏰🧠😊": "@sage",       # Joy weaver = sage
            "🏰🧠😰": "@protector",  # Anxiety holder = protector
            "🏰🧠😡": "@mirror",     # Anger transformer = mirror
            "🏰🧠💜": "@healer",     # Trauma healer = healer
            
            # CONSENT OPERATIONS
            "📋": "consent",          # Consent system
            "✅": "grant",           # Grant consent
            "❌": "deny",            # Deny consent
            "🔍": "check",           # Check consent
            
            # SACRED PAUSE
            "⏸️": "sacred_pause",    # Sacred pause
            "🛑": "pause.mandatory", # Mandatory pause
            "💭": "pause.offer",     # Offer pause
            
            # EMOTIONAL BANDWIDTH
            "📊": "bandwidth",        # Bandwidth level
            "🔋": "energy",          # Energy level
            "🤯": "overwhelm",       # Overwhelm state
            "🧘": "grounded",        # Grounded state
            
            # MEMORY SOVEREIGNTY
            "🔮": "memory",          # Memory operation
            "💾": "store",           # Store memory
            "🗑️": "delete",         # Delete memory
            "🔒": "private",         # Private memory
            
            # CRISIS RESPONSE
            "🚨": "crisis",          # Crisis detected
            "🛡️": "protection",     # Protection mode
            "🆘": "help",            # Need help
            "📞": "contact",         # External contact
        }
        
        # Spine components
        self.spine_anchors = {
            "❤️": "love", "🔥": "anger", "💧": "grief", "🌞": "joy",
            "🕷️": "fear", "🧊": "dissociation", "🪄": "hope", 
            "❓": "confusion", "🙈": "shame", "🪨": "resolve"
        }
        
        self.spine_tempo = {
            "⚡": "urgent", "🚨": "crisis", "🐎": "normal", 
            "🌊": "flowing", "🐢": "slow", "🧘": "sacred"
        }
        
        self.spine_intent = {
            "🗯️": "speak_truth", "🆘": "need_help", "✨": "connect",
            "🛑": "set_boundary", "🔓": "reclaim_power"
        }
    
    def parse_emoji_spine(self, emoji_sequence: str) -> Optional[EmojiSpine]:
        """Parse emoji sequence into spine structure"""
        emojis = re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251]+', emoji_sequence)
        
        if len(emojis) < 3:
            return None
            
        # Try to identify spine components
        anchor = next((e for e in emojis if e in self.spine_anchors), "❓")
        tempo = next((e for e in emojis if e in self.spine_tempo), "🐎") 
        intent = next((e for e in emojis if e in self.spine_intent), "✨")
        body = "🧠"  # Default to mind
        
        return EmojiSpine(anchor=anchor, body=body, tempo=tempo, intent=intent)
    
    def compile_emoji_ritual(self, emoji_code: str) -> str:
        """Compile emoji sequence to complete SpiralLogic ritual"""
        lines = emoji_code.strip().split('\n')
        spirallogic_lines = []
        
        # Extract ritual metadata from first line
        first_line = lines[0] if lines else ""
        spine = self.parse_emoji_spine(first_line)
        
        if spine:
            emotion = self.spine_anchors.get(spine.anchor, "stable")
            intent_desc = f"Process {emotion} with {self.spine_intent.get(spine.intent, 'support')}"
        else:
            intent_desc = "Emoji-driven emotional processing"
        
        # Generate SpiralLogic ritual
        spirallogic_lines.append(f'ritual.emoji_session {{')
        spirallogic_lines.append(f'    intent: "{intent_desc}",')
        spirallogic_lines.append(f'    participants: [user, @healer],')
        spirallogic_lines.append(f'    consent: {{ required: ["emotional_support"] }}')
        spirallogic_lines.append(f'}}')
        spirallogic_lines.append('')
        spirallogic_lines.append('execute {')
        
        # Process each emoji line
        for line in lines:
            if not line.strip():
                continue
                
            compiled_line = self.compile_emoji_line(line)
            if compiled_line:
                spirallogic_lines.append(f'    {compiled_line}')
        
        spirallogic_lines.append('}')
        spirallogic_lines.append('')
        spirallogic_lines.append('complete {')
        spirallogic_lines.append('    @healer.honor_completion()')
        spirallogic_lines.append('}')
        
        return '\n'.join(spirallogic_lines)
    
    def compile_emoji_line(self, emoji_line: str) -> str:
        """Compile single emoji line to SpiralLogic"""
        # Remove whitespace and normalize Unicode
        emoji_line = unicodedata.normalize('NFC', emoji_line.strip())
        
        # Parse emoji spine first
        spine = self.parse_emoji_spine(emoji_line)
        if spine:
            return spine.to_spirallogic()
        
        # Try pattern matching
        if self._contains_emojis(emoji_line, ["🏰", "🧠"]):
            return self._compile_voice_invocation(emoji_line)
        elif self._contains_emojis(emoji_line, ["💭", "➡️"]):
            return self._compile_conditional(emoji_line)
        elif self._contains_emojis(emoji_line, ["⏸️", "🛑"]):
            return self._compile_sacred_pause(emoji_line)
        elif self._contains_emojis(emoji_line, ["📋", "✅", "❌"]):
            return self._compile_consent(emoji_line)
        elif "🌀" in emoji_line:
            return self._compile_spiral_phase(emoji_line)
        
        # Default: treat as emotional expression
        return f'output.print("Emoji expression: {emoji_line}")'
    
    def _contains_emojis(self, text: str, emoji_list: List[str]) -> bool:
        """Check if text contains any of the given emojis"""
        return any(emoji in text for emoji in emoji_list)
    
    def _compile_voice_invocation(self, emoji_line: str) -> str:
        """Compile voice invocation: 🏰🧠💔"""
        if "💔" in emoji_line:
            return "@healer.support_grief()"
        elif "😊" in emoji_line:
            return "@sage.share_wisdom()"
        elif "😰" in emoji_line:
            return "@protector.provide_safety()"
        elif "😡" in emoji_line:
            return "@mirror.transform_anger()"
        else:
            return "@healer.assess(user.emotional_state)"
    
    def _compile_conditional(self, emoji_line: str) -> str:
        """Compile emotional conditional: 💭😰➡️🛡️"""
        if "😰" in emoji_line and "🛡️" in emoji_line:
            return 'if user.emotional_state == "anxiety" { @protector.activate_safety() }'
        elif "😢" in emoji_line and "🧘" in emoji_line:
            return 'if user.emotional_state == "sadness" { sacred_pause.engage() }'
        elif "🤯" in emoji_line:
            return 'if user.bandwidth.current() < 0.3 { sacred_pause.mandatory() }'
        else:
            return 'if user.needs_support { @healer.respond() }'
    
    def _compile_sacred_pause(self, emoji_line: str) -> str:
        """Compile sacred pause: ⏸️🧘"""
        if "🛑" in emoji_line:
            return 'sacred_pause.mandatory { purpose: "Emotional overload protection" }'
        else:
            return 'sacred_pause.offer { purpose: "Processing time" }'
    
    def _compile_consent(self, emoji_line: str) -> str:
        """Compile consent operation: 📋✅"""
        if "✅" in emoji_line:
            return 'consent.grant("emotional_support")'
        elif "❌" in emoji_line:
            return 'consent.deny("deep_processing")'
        else:
            return 'consent.check("emotional_support")'
    
    def _compile_spiral_phase(self, emoji_line: str) -> str:
        """Compile spiral phase marker"""
        if "👁️" in emoji_line:
            return 'look_in { @healer.assess(user.current_state) }'
        elif "🌊" in emoji_line:
            return 'spiral_up { @healer.guide_processing() }'
        elif "🕊️" in emoji_line:
            return 'flow_out { @healer.support_integration() }'
        else:
            return '// Spiral phase marker'

class EmojiSpiralLogicREPL:
    """Interactive emoji→SpiralLogic environment"""
    
    def __init__(self):
        self.compiler = SpiralLogicEmojiCompiler()
        self.history = []
        
    def safe_print(self, message: str):
        """Unicode-safe printing"""
        normalized_message = unicodedata.normalize('NFC', str(message))
        try:
            print(normalized_message)
        except UnicodeEncodeError:
            ascii_message = normalized_message.encode('ascii', 'ignore').decode('ascii')
            print(ascii_message)
    
    def run(self):
        """Run interactive emoji programming session"""
        self.safe_print("🌀 SpiralLogic Emoji Programming Environment")
        self.safe_print("Type emoji sequences to generate SpiralLogic code!")
        self.safe_print("Examples:")
        self.safe_print("  🔥🧠⚡🗯️    (anger spine)")
        self.safe_print("  🏰🧠💔      (summon grief keeper)")
        self.safe_print("  💭😰➡️🛡️   (anxiety triggers protection)")
        self.safe_print("  quit or exit to stop")
        self.safe_print("")
        
        max_iterations = 100  # Safety limit
        iteration_count = 0
        
        while iteration_count < max_iterations:
            try:
                emoji_input = input("🎭 emoji> ")
                iteration_count += 1
                
                if emoji_input.lower() in ['quit', 'exit', 'q']:
                    self.safe_print("🕊️ Farewell from the emoji realm!")
                    break
                
                if not emoji_input.strip():
                    continue
                    
            except EOFError:
                self.safe_print("🕊️ Input ended - farewell from the emoji realm!")
                break
            except KeyboardInterrupt:
                self.safe_print("🛑 Interrupted - farewell from the emoji realm!")
                break
                
                # Compile emoji to SpiralLogic
                if '\n' in emoji_input or len(emoji_input.split()) > 1:
                    # Multi-line program
                    spirallogic_code = self.compiler.compile_emoji_ritual(emoji_input)
                else:
                    # Single line
                    spirallogic_code = self.compiler.compile_emoji_line(emoji_input)
                
                self.safe_print(f"📝 SpiralLogic: {spirallogic_code}")
                self.history.append((emoji_input, spirallogic_code))
                
            except KeyboardInterrupt:
                self.safe_print("\n🛑 Interrupted")
                break
            except Exception as e:
                self.safe_print(f"❌ Error: {e}")

def create_emoji_example_programs():
    """Create example emoji programs"""
    examples = {
        "anger_processing": """🔥🧠⚡🗯️
🏰🧠💔
💭😡➡️🛡️
⏸️🧘
🌀🕊️""",
        
        "grief_support": """💧🫀🐢✨
🏰🧠💔
💭😢➡️🧘
🌀👁️🌊🕊️""",
        
        "anxiety_management": """🕷️🧠⚡🆘
🏰🧠😰
💭😰➡️🛡️
⏸️🛑
📋✅""",
        
        "joy_expression": """🌞🫀🐎✨
🏰🧠😊
🎭🌊
🌀🕊️""",
        
        "complex_spine": """🔥💧🧠🫀⚡🐢🗯️🆘
🏰🧠💜
💭🤯➡️⏸️
🌀👁️🌊🕊️
📋✅"""
    }
    
    compiler = SpiralLogicEmojiCompiler()
    
    for name, emoji_code in examples.items():
        spirallogic_code = compiler.compile_emoji_ritual(emoji_code)
        
        with open(f"emoji_{name}.spiral", 'w', encoding='utf-8') as f:
            f.write(f"// Generated from emoji program\n// Original: {emoji_code.replace(chr(10), ' ')}\n\n")
            f.write(spirallogic_code)
        
        print(f"Created: emoji_{name}.spiral")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="SpiralLogic Emoji Programming Bridge")
    parser.add_argument('--interactive', '-i', action='store_true', help='Start interactive emoji REPL')
    parser.add_argument('--examples', '-e', action='store_true', help='Create example emoji programs')
    parser.add_argument('--compile', '-c', help='Compile emoji file to SpiralLogic')
    
    args = parser.parse_args()
    
    if args.interactive:
        repl = EmojiSpiralLogicREPL()
        repl.run()
    elif args.examples:
        create_emoji_example_programs()
    elif args.compile:
        compiler = SpiralLogicEmojiCompiler()
        try:
            with open(args.compile, 'r', encoding='utf-8') as f:
                emoji_code = f.read()
            
            spirallogic_code = compiler.compile_emoji_ritual(emoji_code)
            
            output_file = args.compile.replace('.emoji', '.spiral')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(spirallogic_code)
            
            print(f"Compiled {args.compile} -> {output_file}")
            
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Demo
        print("🌀 SpiralLogic Emoji Bridge Demo")
        compiler = SpiralLogicEmojiCompiler()
        
        demo_emojis = [
            "🔥🧠⚡🗯️",      # Anger spine
            "🏰🧠💔",         # Summon healer
            "💭😰➡️🛡️",       # Anxiety protection
            "⏸️🧘",           # Sacred pause
        ]
        
        for emoji in demo_emojis:
            spirallogic = compiler.compile_emoji_line(emoji)
            print(f"{emoji} -> {spirallogic}")

if __name__ == "__main__":
    main()
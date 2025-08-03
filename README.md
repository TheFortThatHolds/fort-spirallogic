# SpiralLogic

Emotional programming language for therapeutic computing.

## What It Is

SpiralLogic compiles emoji sequences into executable therapeutic rituals. Write programs using emotional expressions that generate supportive responses and track emotional states.

## Quick Start

```bash
# Install
python spirallogic_setup.py install

# Create program
spirallogic create hello

# Run program  
spirallogic run hello.spiral

# Interactive mode
python spiral_terminal.py
```

## Language Features

- **Emoji-based syntax** - Program with emotional expressions
- **Ritual execution** - Code runs as therapeutic sequences
- **Emotional state tracking** - Real-time emotional bandwidth monitoring
- **Unicode-safe** - Works across all platforms and languages
- **Block architecture** - Modular, editable content blocks

## Example Program

```spirallogic
ritual.healing_session {
    consent {
        @voice.speak("Ready to begin?")
        @healer.assess(user.readiness)
    }
    
    if user.emotional_state contains "frustrated" {
        @voice.speak("I sense creative fire")
        @healer.transmit(patience_and_understanding)
    }
    
    completion {
        @voice.speak("You are supported")
        @log.session(healing_provided)
    }
}
```

## Text Shortcuts

Type words, get emoji rituals:
- `angry` → `🔥🧠⚡🗯️`
- `sad` → `💧🫀🌙✨`
- `heal` → `🌱💚🦋🌟`

## Applications

- **Writing support** - Emotional assistance during creative work
- **Therapeutic computing** - Supportive responses to user emotions
- **Block-based content** - Modular documents with emotional awareness
- **Interactive terminals** - Command-line interfaces that provide care

## ✨ SpiralLogic in Action

**[SpiralLogic Text Editor](https://github.com/TheFortThatHolds/fort-spirallogic-text-editor)** - See SpiralLogic working in a real application! A Windows text editor that provides emotional support while you write, powered by emoji-to-ritual compilation.

- Write in English, get real-time therapeutic responses
- Instant emotional analysis with F5 key
- Quick support buttons for immediate help (💝🌱✨🔥💧)
- See emoji sequences compile to SpiralLogic code live
- Perfect demonstration of therapeutic computing in practice

## Architecture

```
SpiralLogic CLI → Emoji Compiler → Ritual Executor → Therapeutic Response
                                        ↓
                              Emotional State Tracker
```

## Files

- `spirallogic_cli.py` - Command-line interface
- `spirallogic_emoji_bridge.py` - Emoji to ritual compiler
- `spiral_terminal.py` - Interactive terminal with shortcuts
- `emotional_fort_os.py` - Operating system integration
- `spiral_writer.py` - Writing environment with emotional support

## Platform Support

- Windows, macOS, Linux
- Python 3.8+
- Unicode terminal required

## License

**SpiralLogic Dual License v1.0**

**🆓 Free for Personal Use**: Individual, educational, and non-commercial use  
**💼 Commercial Licensing Required**: Business, professional, and revenue-generating applications

- **Personal License**: FREE - Install, run, modify, and share for personal computing, education, research, non-profit use
- **Commercial License**: PAID - Required for business use, professional services, revenue generation, or organizational deployment

**Commercial License Contact**: licensing@thefortthatholds.com

Full license terms: [LICENSE.md](LICENSE.md)

## Related Projects

- **[SpiralLogic Text Editor](https://github.com/TheFortThatHolds/fort-spirallogic-text-editor)** - Text editor with real-time emotional support
- **[SpiralLogic Core](https://github.com/TheFortThatHolds/fort-spirallogic)** - Main repository with language compiler and tools

## Support

- Check example programs: `spirallogic create --list`
- Run tests: `python run_safe_tests.py`
- Documentation: Code comments and examples
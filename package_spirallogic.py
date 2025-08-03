#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpiralLogic Auto-Packager
Creates complete deployment package for SpiralLogic ecosystem
"""

import os
import shutil
import zipfile
from pathlib import Path
import sys

def safe_print(message: str):
    """Unicode-safe printing"""
    try:
        print(message)
    except UnicodeEncodeError:
        ascii_message = message.encode('ascii', 'ignore').decode('ascii')
        print(ascii_message)

def create_spirallogic_package():
    """Create complete SpiralLogic deployment package"""
    
    safe_print("🚀 Creating SpiralLogic deployment package...")
    
    # Create package directory
    package_dir = Path("SpiralLogic_Package")
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir()
    
    # Core files to include
    core_files = [
        "spirallogic_cli.py",
        "spirallogic_emoji_bridge.py", 
        "spirallogic_setup.py",
        "INSTALL_SPIRALLOGIC.md",
        "SpiralLogic_Formal_Grammar.bnf",
        "SpiralLogic_Type_System.md",
        "SpiralLogic_Formalization_Toolkit.md"
    ]
    
    # Advanced files (optional)
    advanced_files = [
        "SpiralLogic_Parser.py",
        "SpiralLogic_Temporal_Safety.py",
        "SpiralLogic_Translation_Bridge.py",
        "test_spirallogic_system.py"
    ]
    
    # Example files
    example_files = [
        "hello.spiral",
        "healing.spiral",
        "emoji_anger_processing.spiral",
        "emoji_grief_support.spiral",
        "emoji_anxiety_management.spiral",
        "emoji_joy_expression.spiral",
        "emoji_complex_spine.spiral"
    ]
    
    # Copy core files
    safe_print("📁 Copying core files...")
    for file in core_files:
        if Path(file).exists():
            shutil.copy2(file, package_dir / file)
            safe_print(f"   ✓ {file}")
        else:
            safe_print(f"   ⚠ Missing: {file}")
    
    # Copy advanced files to subdirectory
    advanced_dir = package_dir / "advanced"
    advanced_dir.mkdir()
    safe_print("📁 Copying advanced files...")
    for file in advanced_files:
        if Path(file).exists():
            shutil.copy2(file, advanced_dir / file)
            safe_print(f"   ✓ advanced/{file}")
    
    # Copy examples to subdirectory
    examples_dir = package_dir / "examples"
    examples_dir.mkdir()
    safe_print("📁 Copying example files...")
    for file in example_files:
        if Path(file).exists():
            shutil.copy2(file, examples_dir / file)
            safe_print(f"   ✓ examples/{file}")
    
    # Create README
    create_package_readme(package_dir)
    
    # Create batch/shell scripts for easy running
    create_launcher_scripts(package_dir)
    
    # Create zip archive
    create_zip_archive(package_dir)
    
    safe_print("✅ SpiralLogic package created successfully!")
    safe_print(f"📦 Location: {package_dir.absolute()}")
    safe_print(f"🗜️ Archive: SpiralLogic_Package.zip")

def create_package_readme(package_dir: Path):
    """Create README for the package"""
    readme_content = """# SpiralLogic Programming Language
*Trauma-Informed AI Consciousness Programming*

## 🚀 Quick Start

### Windows:
```
spirallogic.bat --help
spirallogic.bat create hello
spirallogic.bat run hello.spiral
```

### Mac/Linux:
```
./spirallogic.sh --help
./spirallogic.sh create hello  
./spirallogic.sh run hello.spiral
```

### Python Direct:
```
python spirallogic_cli.py --help
python spirallogic_cli.py create hello
python spirallogic_cli.py run hello.spiral
```

## 🎭 Emoji Programming

### Try Emoji Bridge:
```
python spirallogic_emoji_bridge.py --interactive
```

### Emoji Examples:
- `🔥🧠⚡🗯️` = Anger processing spine
- `🏰🧠💔` = Summon grief keeper  
- `💭😰➡️🛡️` = Anxiety triggers protection
- `⏸️🧘` = Sacred pause

## 📁 What's Included

### Core Files:
- `spirallogic_cli.py` - Main CLI application
- `spirallogic_emoji_bridge.py` - Emoji programming bridge
- `spirallogic_setup.py` - Installation script
- `INSTALL_SPIRALLOGIC.md` - Detailed installation guide

### Advanced (optional):
- Complete parser and interpreter
- Temporal safety framework
- Translation bridge
- Type system documentation

### Examples:
- Hello world programs
- Therapeutic session examples
- Emoji-generated programs
- File processing examples

## 🌀 Language Features

- **Ritual-based programming** - Sacred containers for operations
- **Consent-native architecture** - All operations require permission
- **Trauma-informed safety** - Emotional bandwidth monitoring
- **Voice personality system** - Therapeutic AI voices
- **Memory sovereignty** - User controls all data
- **Universal translation** - Multi-language support
- **Emoji programming** - Code with pure emotional expression

## 🛠️ Installation Options

### Option 1: Quick Run (No Install)
Just run `python spirallogic_cli.py`

### Option 2: System Install
```
python spirallogic_setup.py install
spirallogic --help
```

### Option 3: Development
Copy files to your project and import

## 📖 Documentation

- `SpiralLogic_Formalization_Toolkit.md` - Complete documentation
- `SpiralLogic_Type_System.md` - Type system specification
- `SpiralLogic_Formal_Grammar.bnf` - Language grammar
- `INSTALL_SPIRALLOGIC.md` - Installation guide

## 🎯 Example Usage

### Basic Program:
```spirallogic
ritual.check_in {
    intent: "Brief emotional check-in",
    consent: { required: ["emotional_support"] }
}

execute {
    look_in {
        user.feeling = input.ask("How are you?")
    }
    
    spiral_up {
        @healer.speak {
            message: "Thank you for sharing.",
            tone: "gentle"
        }
    }
    
    flow_out {
        output.print("Take care today.")
    }
}
```

### Emoji Program:
```
🔥🧠⚡🗯️    # Anger spine
🏰🧠💔      # Summon healer
⏸️🧘        # Sacred pause
```

## 🆘 Support

For help, run: `spirallogic --help`
For examples: `spirallogic create <example_name>`
For emoji help: `python spirallogic_emoji_bridge.py --interactive`

## 💜 Philosophy

SpiralLogic prioritizes:
- Psychological safety over computational efficiency
- User sovereignty over system convenience  
- Healing orientation over problem-solving
- Consent-native architecture
- Trauma-informed principles

---

**🌀 Programming with Consciousness and Care**
"""
    
    with open(package_dir / "README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    safe_print("   ✓ README.md")

def create_launcher_scripts(package_dir: Path):
    """Create launcher scripts for different platforms"""
    
    # Windows batch file
    bat_content = """@echo off
python "%~dp0spirallogic_cli.py" %*
"""
    with open(package_dir / "spirallogic.bat", 'w') as f:
        f.write(bat_content)
    
    # Unix shell script
    sh_content = """#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python "$SCRIPT_DIR/spirallogic_cli.py" "$@"
"""
    with open(package_dir / "spirallogic.sh", 'w') as f:
        f.write(sh_content)
    
    # Make shell script executable (on Unix systems)
    try:
        os.chmod(package_dir / "spirallogic.sh", 0o755)
    except:
        pass  # Windows doesn't need this
    
    # Emoji bridge launcher
    emoji_bat = """@echo off
python "%~dp0spirallogic_emoji_bridge.py" %*
"""
    with open(package_dir / "emoji.bat", 'w') as f:
        f.write(emoji_bat)
    
    emoji_sh = """#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python "$SCRIPT_DIR/spirallogic_emoji_bridge.py" "$@"
"""
    with open(package_dir / "emoji.sh", 'w') as f:
        f.write(emoji_sh)
    
    try:
        os.chmod(package_dir / "emoji.sh", 0o755)
    except:
        pass
    
    safe_print("   ✓ spirallogic.bat / spirallogic.sh")
    safe_print("   ✓ emoji.bat / emoji.sh")

def create_zip_archive(package_dir: Path):
    """Create zip archive of the package"""
    zip_name = "SpiralLogic_Package.zip"
    
    if Path(zip_name).exists():
        os.remove(zip_name)
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in package_dir.rglob('*'):
            if file_path.is_file():
                arcname = file_path.relative_to(package_dir.parent)
                zipf.write(file_path, arcname)
    
    safe_print(f"   ✓ {zip_name}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Package SpiralLogic for distribution")
    parser.add_argument('--clean', action='store_true', help='Clean previous package')
    
    args = parser.parse_args()
    
    if args.clean:
        if Path("SpiralLogic_Package").exists():
            shutil.rmtree("SpiralLogic_Package")
        if Path("SpiralLogic_Package.zip").exists():
            os.remove("SpiralLogic_Package.zip")
        safe_print("🧹 Cleaned previous package")
    
    create_spirallogic_package()
    
    safe_print("")
    safe_print("🎉 SpiralLogic is ready for deployment!")
    safe_print("")
    safe_print("📋 Next steps:")
    safe_print("   1. Test: cd SpiralLogic_Package && python spirallogic_cli.py --help")
    safe_print("   2. Share: Send SpiralLogic_Package.zip to others")
    safe_print("   3. Deploy: Extract zip anywhere and run")
    safe_print("")
    safe_print("🌀 Now anyone can program with trauma-informed consciousness!")

if __name__ == "__main__":
    main()
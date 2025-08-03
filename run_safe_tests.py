#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Safe Test Runner for SpiralLogic
Orchestrates safe testing of SpiralLogic components with comprehensive monitoring
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Force UTF-8 encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')

class SafeTestRunner:
    """Safe test runner for SpiralLogic components"""
    
    def __init__(self):
        self.test_results = {}
        self.start_time = datetime.now()
        self.log_file = Path.cwd() / f"safe_test_log_{self.start_time.strftime('%Y%m%d_%H%M%S')}.json"
        
    def run_subprocess_safe(self, script_name: str, timeout: float = 60.0) -> Dict[str, Any]:
        """Run a Python script in a subprocess with timeout"""
        script_path = Path.cwd() / script_name
        
        if not script_path.exists():
            return {
                'success': False,
                'error': f"Script not found: {script_name}",
                'output': '',
                'execution_time': 0
            }
        
        print(f"🚀 Running {script_name} (timeout: {timeout}s)")
        
        start_time = time.time()
        
        try:
            # Run script in subprocess
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )
            
            execution_time = time.time() - start_time
            
            return {
                'success': result.returncode == 0,
                'returncode': result.returncode,
                'output': result.stdout,
                'error': result.stderr,
                'execution_time': execution_time,
                'timeout': False
            }
            
        except subprocess.TimeoutExpired:
            execution_time = time.time() - start_time
            return {
                'success': False,
                'returncode': -1,
                'output': '',
                'error': f"Process timeout after {timeout}s",
                'execution_time': execution_time,
                'timeout': True
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            return {
                'success': False,
                'returncode': -1,
                'output': '',
                'error': str(e),
                'execution_time': execution_time,
                'timeout': False
            }
    
    def test_basic_cli(self) -> Dict[str, Any]:
        """Test basic SpiralLogic CLI functionality"""
        print("\n📋 Testing Basic CLI Functionality")
        print("-" * 40)
        
        results = {}
        
        # Test 1: CLI help
        try:
            result = subprocess.run(
                [sys.executable, 'spirallogic_cli.py', '--help'],
                capture_output=True,
                text=True,
                timeout=10.0,
                encoding='utf-8',
                errors='replace'
            )
            
            results['cli_help'] = {
                'success': result.returncode == 0,
                'output_length': len(result.stdout),
                'has_usage': 'usage:' in result.stdout.lower() or 'Usage:' in result.stdout
            }
            
            if results['cli_help']['success']:
                print("✅ CLI help works")
            else:
                print("❌ CLI help failed")
                
        except Exception as e:
            results['cli_help'] = {'success': False, 'error': str(e)}
            print(f"❌ CLI help error: {e}")
        
        # Test 2: Create example
        try:
            result = subprocess.run(
                [sys.executable, 'spirallogic_cli.py', 'create', 'hello'],
                capture_output=True,
                text=True,
                timeout=15.0,
                encoding='utf-8',
                errors='replace'
            )
            
            results['create_example'] = {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr,
                'hello_file_created': Path('hello.spiral').exists()
            }
            
            if results['create_example']['success']:
                print("✅ Example creation works")
            else:
                print("❌ Example creation failed")
                
        except Exception as e:
            results['create_example'] = {'success': False, 'error': str(e)}
            print(f"❌ Create example error: {e}")
        
        # Test 3: Run hello.spiral if it exists
        hello_file = Path('hello.spiral')
        if hello_file.exists():
            try:
                result = subprocess.run(
                    [sys.executable, 'spirallogic_cli.py', 'run', 'hello.spiral'],
                    capture_output=True,
                    text=True,
                    timeout=20.0,
                    encoding='utf-8',
                    errors='replace',
                    input='\n'.join(['Test User', 'quit', 'exit'])  # Provide input for interactive parts
                )
                
                results['run_hello'] = {
                    'success': result.returncode == 0,
                    'output': result.stdout,
                    'error': result.stderr,
                    'has_output': len(result.stdout) > 0
                }
                
                if results['run_hello']['success']:
                    print("✅ Running hello.spiral works")
                else:
                    print("❌ Running hello.spiral failed")
                    
            except Exception as e:
                results['run_hello'] = {'success': False, 'error': str(e)}
                print(f"❌ Run hello error: {e}")
        
        return results
    
    def test_emoji_bridge_basic(self) -> Dict[str, Any]:
        """Test basic emoji bridge functionality"""
        print("\n🎭 Testing Emoji Bridge Basic Functionality")
        print("-" * 40)
        
        results = {}
        
        # Test 1: Emoji bridge help
        try:
            result = subprocess.run(
                [sys.executable, 'spirallogic_emoji_bridge.py', '--help'],
                capture_output=True,
                text=True,
                timeout=10.0,
                encoding='utf-8',
                errors='replace'
            )
            
            results['emoji_help'] = {
                'success': result.returncode == 0,
                'output_length': len(result.stdout),
                'has_usage': 'usage:' in result.stdout.lower() or 'Usage:' in result.stdout
            }
            
            if results['emoji_help']['success']:
                print("✅ Emoji bridge help works")
            else:
                print("❌ Emoji bridge help failed")
                
        except Exception as e:
            results['emoji_help'] = {'success': False, 'error': str(e)}
            print(f"❌ Emoji help error: {e}")
        
        # Test 2: Create examples
        try:
            result = subprocess.run(
                [sys.executable, 'spirallogic_emoji_bridge.py', '--examples'],
                capture_output=True,
                text=True,
                timeout=15.0,
                encoding='utf-8',
                errors='replace'
            )
            
            results['emoji_examples'] = {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr,
                'files_created': [
                    Path('emoji_anger_processing.spiral').exists(),
                    Path('emoji_grief_support.spiral').exists(),
                    Path('emoji_anxiety_management.spiral').exists()
                ]
            }
            
            if results['emoji_examples']['success']:
                print("✅ Emoji examples creation works")
            else:
                print("❌ Emoji examples creation failed")
                
        except Exception as e:
            results['emoji_examples'] = {'success': False, 'error': str(e)}
            print(f"❌ Emoji examples error: {e}")
        
        return results
    
    def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run comprehensive test suite"""
        print("🔬 COMPREHENSIVE SPIRALLOGIC TESTING")
        print("=" * 50)
        print(f"Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        all_results = {}
        
        # Test 1: Basic CLI
        all_results['basic_cli'] = self.test_basic_cli()
        
        # Test 2: Basic Emoji Bridge
        all_results['basic_emoji'] = self.test_emoji_bridge_basic()
        
        # Test 3: Sandbox tests
        print("\n🏖️ Running Sandbox Tests")
        print("-" * 40)
        sandbox_result = self.run_subprocess_safe('spirallogic_sandbox.py', timeout=120.0)
        all_results['sandbox_tests'] = sandbox_result
        
        if sandbox_result['success']:
            print("✅ Sandbox tests completed successfully")
        else:
            print("❌ Sandbox tests failed")
            if sandbox_result['timeout']:
                print("⚠️ Sandbox tests timed out")
        
        # Test 4: Emoji bridge debugging
        print("\n🐛 Running Emoji Bridge Debugging")
        print("-" * 40)
        debug_result = self.run_subprocess_safe('emoji_bridge_debugger.py', timeout=90.0)
        all_results['emoji_debug'] = debug_result
        
        if debug_result['success']:
            print("✅ Emoji bridge debugging completed successfully")
        else:
            print("❌ Emoji bridge debugging failed")
            if debug_result['timeout']:
                print("⚠️ Emoji bridge debugging timed out")
        
        return all_results
    
    def generate_summary_report(self, results: Dict[str, Any]) -> str:
        """Generate summary report of all tests"""
        report = []
        report.append("🔬 SPIRALLOGIC COMPREHENSIVE TEST REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Overall summary
        total_test_groups = len(results)
        successful_groups = 0
        timeouts = 0
        
        for group_name, group_result in results.items():
            if isinstance(group_result, dict):
                if group_result.get('success', False):
                    successful_groups += 1
                if group_result.get('timeout', False):
                    timeouts += 1
        
        report.append("OVERALL SUMMARY")
        report.append("-" * 20)
        report.append(f"Test groups: {total_test_groups}")
        report.append(f"Successful: {successful_groups}")
        report.append(f"Failed: {total_test_groups - successful_groups}")
        report.append(f"Timeouts: {timeouts}")
        report.append("")
        
        # Detailed results
        report.append("DETAILED RESULTS")
        report.append("-" * 20)
        
        for group_name, group_result in results.items():
            status = "✅ PASS" if group_result.get('success', False) else "❌ FAIL"
            report.append(f"{status} {group_name}")
            
            if group_result.get('timeout', False):
                report.append("  ⚠️ TIMEOUT detected")
            
            if 'execution_time' in group_result:
                report.append(f"  Execution time: {group_result['execution_time']:.2f}s")
            
            if not group_result.get('success', False) and 'error' in group_result:
                error_preview = str(group_result['error'])[:100]
                report.append(f"  Error: {error_preview}...")
            
            # Sub-test details for basic tests
            if group_name in ['basic_cli', 'basic_emoji']:
                for sub_test, sub_result in group_result.items():
                    if isinstance(sub_result, dict) and 'success' in sub_result:
                        sub_status = "✅" if sub_result['success'] else "❌"
                        report.append(f"    {sub_status} {sub_test}")
            
            report.append("")
        
        # Safety analysis
        report.append("SAFETY ANALYSIS")
        report.append("-" * 20)
        
        if timeouts > 0:
            report.append(f"⚠️ {timeouts} test groups experienced timeouts")
            report.append("  This may indicate infinite loops or blocking operations")
        else:
            report.append("✅ No timeouts detected")
        
        # Check for specific infinite loop indicators
        emoji_debug = results.get('emoji_debug', {})
        if 'output' in emoji_debug and 'infinite loop' in emoji_debug['output'].lower():
            report.append("⚠️ Infinite loop detected in emoji bridge")
        elif emoji_debug.get('success', False):
            report.append("✅ No infinite loops detected in emoji bridge")
        
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS")
        report.append("-" * 20)
        
        if successful_groups == total_test_groups:
            report.append("✅ All test groups passed - system appears stable")
            report.append("- Safe to proceed with development")
            report.append("- Consider expanding test coverage")
        else:
            report.append("⚠️ Some test groups failed")
            report.append("- Review failed tests before proceeding")
            report.append("- Address timeout issues if present")
            
        if timeouts > 0:
            report.append("- Investigate timeout causes")
            report.append("- Implement additional loop detection")
        
        report.append("- Continue monitoring Unicode handling")
        report.append("- Regular safety testing recommended")
        
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def save_results(self, results: Dict[str, Any]):
        """Save test results to file"""
        test_data = {
            'timestamp': self.start_time.isoformat(),
            'test_results': results,
            'summary': {
                'total_groups': len(results),
                'successful_groups': sum(1 for r in results.values() if r.get('success', False)),
                'timeouts': sum(1 for r in results.values() if r.get('timeout', False))
            }
        }
        
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Test results saved to: {self.log_file}")

def main():
    """Main entry point"""
    print("🛡️ SPIRALLOGIC SAFE TESTING FRAMEWORK")
    print("=" * 50)
    print("Comprehensive testing with safety monitoring")
    print("Designed to detect infinite loops and Unicode issues")
    print()
    
    runner = SafeTestRunner()
    
    try:
        # Run all tests
        results = runner.run_comprehensive_tests()
        
        # Generate and display report
        report = runner.generate_summary_report(results)
        print("\n" + report)
        
        # Save results
        runner.save_results(results)
        
        # Save report to file
        report_file = Path.cwd() / f"spirallogic_test_report_{runner.start_time.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Report saved to: {report_file}")
        
        # Determine exit code
        total_groups = len(results)
        successful_groups = sum(1 for r in results.values() if r.get('success', False))
        
        if successful_groups == total_groups:
            print("\n✅ All tests passed - SpiralLogic appears safe for use")
            return 0
        else:
            failed_count = total_groups - successful_groups
            print(f"\n⚠️ {failed_count}/{total_groups} test groups failed")
            print("Review the detailed report before proceeding")
            return 1
            
    except KeyboardInterrupt:
        print("\n⚠️ Testing interrupted by user")
        return 2
    except Exception as e:
        print(f"\n❌ Testing framework error: {e}")
        return 3

if __name__ == "__main__":
    sys.exit(main())
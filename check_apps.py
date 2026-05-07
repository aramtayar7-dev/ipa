#!/usr/bin/env python3
"""
Validation script for checking all app download URLs in apps.json
سکریپتی پشکنینی بۆ دڵنیابوونەوە لەوێی هەموو لینکەکانی داونلۆد کاردەکەن
"""

import json
import requests
import sys
from datetime import datetime
from pathlib import Path


def load_apps_json(filepath="apps.json"):
    """Load and parse the apps.json file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ خرۆپە: فایلی {filepath} دۆزی نەهات")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ خرۆپە لە JSON: {e}")
        sys.exit(1)


def check_url(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code < 400, response.status_code
    except requests.exceptions.Timeout:
        return False, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return False, "CONNECTION_ERROR"
    except Exception as e:
        return False, str(e)


def validate_app(app, index):
    """Validate a single app entry"""
    errors = []
    warnings = []
    
    # Check required fields
    required_fields = ['name', 'bundleIdentifier', 'version', 'downloadURL', 'developerName']
    for field in required_fields:
        if field not in app or not app[field]:
            errors.append(f"❌ ناکۆکی: فیلدی '{field}' نیە یان بەتاڵە")
    
    # Check icon URL
    if 'iconURL' not in app or not app['iconURL']:
        warnings.append(f"⚠️  ھشیار: وێنەی ئایکۆن نیە")
    
    # Check bundle identifier format
    if 'bundleIdentifier' in app:
        bundle = app['bundleIdentifier']
        if not (bundle.count('.') >= 1 and all(part.replace('-', '').isalnum() for part in bundle.split('.'))):
            warnings.append(f"⚠️  ھشیار: Bundle Identifier فۆرمات غیر معیاری: {bundle}")
    
    # Check size
    if app.get('size', 0) < 1000000:  # Less than 1MB is suspicious
        warnings.append(f"⚠️  ھشیار: قەبارەی بەرنامە کچووکە: {app.get('size', 0)} bytes")
    
    return errors, warnings


def main():
    print("=" * 70)
    print("🔍 سکریپتی پشکنینی Guevara App Store")
    print("=" * 70)
    print()
    
    # Load apps
    data = load_apps_json()
    apps = data.get('apps', [])
    
    print(f"📊 کۆی بەرنامەکان: {len(apps)}")
    print(f"📝 ئیدینتیفایر: {data.get('identifier', 'نیشتمان نیە')}")
    print(f"🔗 ئۆندەرێس: {data.get('sourceURL', 'نیشتمان نیە')}")
    print()
    
    total_errors = 0
    total_warnings = 0
    failed_urls = []
    
    # Validate each app
    for i, app in enumerate(apps, 1):
        print(f"[{i}/{len(apps)}] {app.get('name', 'بێناو')}")
        
        # Validate structure
        errors, warnings = validate_app(app, i)
        
        if errors:
            total_errors += len(errors)
            for error in errors:
                print(f"    {error}")
        
        if warnings:
            total_warnings += len(warnings)
            for warning in warnings:
                print(f"    {warning}")
        
        # Check download URL (only if downloadURL exists)
        if 'downloadURL' in app and app['downloadURL']:
            print(f"    🔗 پشکنینی لینکی داونلۆد...")
            is_valid, status = check_url(app['downloadURL'])
            
            if is_valid:
                if status == 200:
                    print(f"    ✅ لینکی داونلۆد کاردە")
                else:
                    print(f"    ✓ لینکی داونلۆد وەبابێت (کۆدی: {status})")
            else:
                total_errors += 1
                print(f"    ❌ لینکی داونلۆد غیر دەستچوو: {status}")
                failed_urls.append((app.get('name'), app['downloadURL'], status))
        
        # Check icon URL (only if iconURL exists)
        if 'iconURL' in app and app['iconURL'] and 'raw.githubusercontent.com' not in app['iconURL']:
            print(f"    🎨 پشکنینی لینکی وێنە...")
            is_valid, status = check_url(app['iconURL'], timeout=5)
            
            if is_valid:
                print(f"    ✅ وێنە دەستچوو")
            else:
                total_warnings += 1
                print(f"    ⚠️  وێنە غیر دەستچوو: {status}")
        
        print()
    
    # Summary
    print("=" * 70)
    print("📋 خلاسەکە:")
    print(f"✅ کۆی بەرنامەکان: {len(apps)}")
    print(f"❌ کۆی خرۆپەکان: {total_errors}")
    print(f"⚠️  کۆی ھشیاریەکان: {total_warnings}")
    print()
    
    if failed_urls:
        print("🔴 لینکەکانی شکاو:")
        for name, url, status in failed_urls:
            print(f"  • {name}: {status}")
        print()
    
    # Final verdict
    if total_errors == 0:
        print("✅ هەموو پشکنینەکان سەرکەوتو بوون!")
        return 0
    else:
        print(f"❌ {total_errors} خرۆپە دۆزی هات!")
        return 1


if __name__ == "__main__":
    sys.exit(main())

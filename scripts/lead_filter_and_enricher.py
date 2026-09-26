# -*- coding: utf-8 -*-
"""
B2B Lead Filter and Validation Tool
用于本地批量清洗外贸潜在客户名单、检测官网存活状态、正负向关键词过滤及邮箱格式校验。
"""

import os
import re
import urllib.request
import urllib.error
import ssl

ssl_context = ssl._create_unverified_context()

DEFAULT_NEGATIVE_KEYWORDS = [
    'furniture', 'sofa', 'clothing', 'apparel', 'textile', 
    'machinery', 'automotive', 'industrial seal', 'o-ring', 'electronics'
]

def check_domain_alive(url, timeout=5):
    """验证网站是否可以正常连通且不是死链"""
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as response:
            return response.status in [200, 301, 302], response.geturl()
    except Exception:
        return False, None

def is_valid_email(email):
    """校验是否是合法的商业邮箱"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email).strip()))

def filter_lead(company_name, description, negative_keywords=None):
    """根据负向词排雷"""
    if negative_keywords is None:
        negative_keywords = DEFAULT_NEGATIVE_KEYWORDS
    text_to_check = f"{company_name} {description}".lower()
    for neg in negative_keywords:
        if neg.lower() in text_to_check:
            return False, f"Hit negative keyword: {neg}"
    return True, "Passed"

if __name__ == '__main__':
    print("B2B Lead Filter Tool initialized successfully.")


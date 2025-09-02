// lib/services/wordpress_service.dart

import 'dart:convert';

import 'package:http/http.dart' as http;

import '../models/wordpress_config.dart';

class WordPressService {
  final WordPressConfig config;

  WordPressService({required this.config});

  Future<Map<String, dynamic>> publishPost({
    required String title,
    required String content,
    String status = 'draft',
    List<int>? categories,
    List<int>? tags,
    String excerpt = '',
  }) async {
    // 准备API URL
    final apiUrl = '${config.siteUrl}/wp-json/wp/v2/posts';

    // 准备Basic Auth认证头
    final credentials = '${config.username}:${config.appPassword}';
    final token = base64Encode(utf8.encode(credentials));

    // 准备请求头
    final headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic $token',
      'User-Agent': 'WordPress-Publisher-Flutter/1.0'
    };

    // 准备请求体 - 使用 Map<String, dynamic> 类型
    final Map<String, dynamic> body = {
      'title': title,
      'content': content,
      'status': status,
      'excerpt': excerpt,
    };

    // 添加可选分类和标签 - 确保使用正确的类型
    if (categories != null && categories.isNotEmpty) {
      body['categories'] = categories;
    }
    if (tags != null && tags.isNotEmpty) {
      body['tags'] = tags;
    }

    try {
      // 发送POST请求
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: headers,
        body: json.encode(body), // 使用 json.encode 转换整个 body
      );

      if (response.statusCode == 201) {
        // 发布成功
        return {
          'success': true,
          'data': json.decode(response.body),
        };
      } else {
        // 发布失败
        return {
          'success': false,
          'error': '发布失败，状态码: ${response.statusCode}',
          'details': response.body,
        };
      }
    } catch (e) {
      // 请求过程中出现错误
      return {
        'success': false,
        'error': '请求过程中出现错误: $e',
      };
    }
  }

  // 测试连接
  Future<bool> testConnection() async {
    try {
      final apiUrl = '${config.siteUrl}/wp-json/wp/v2/categories';
      final credentials = '${config.username}:${config.appPassword}';
      final token = base64Encode(utf8.encode(credentials));

      final headers = {
        'Authorization': 'Basic $token',
      };

      final response = await http.get(Uri.parse(apiUrl), headers: headers);
      return response.statusCode == 200;
    } catch (e) {
      return false;
    }
  }
}
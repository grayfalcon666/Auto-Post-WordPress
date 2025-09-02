import 'package:flutter/material.dart';

import '../models/wordpress_config.dart';
import '../services/wordpress_service.dart';

class PublishScreen extends StatefulWidget {
  final WordPressConfig config;

  const PublishScreen({Key? key, required this.config}) : super(key: key);

  @override
  _PublishScreenState createState() => _PublishScreenState();
}

class _PublishScreenState extends State<PublishScreen> {
  final _formKey = GlobalKey<FormState>();
  final _titleController = TextEditingController();
  final _contentController = TextEditingController();
  final _categoriesController = TextEditingController();
  final _tagsController = TextEditingController();
  final _excerptController = TextEditingController();

  String _status = 'draft';
  bool _isPublishing = false;

  Future<void> _publishPost() async {
    if (_formKey.currentState!.validate()) {
      setState(() {
        _isPublishing = true;
      });

      final service = WordPressService(config: widget.config);

      // 解析分类和标签
      List<int>? categories;
      if (_categoriesController.text.isNotEmpty) {
        categories = _categoriesController.text
            .split(',')
            .map((e) => int.tryParse(e.trim()) ?? 0)
            .where((id) => id > 0)
            .toList();
        if (categories.isEmpty) categories = null;
      }

      List<int>? tags;
      if (_tagsController.text.isNotEmpty) {
        tags = _tagsController.text
            .split(',')
            .map((e) => int.tryParse(e.trim()) ?? 0)
            .where((id) => id > 0)
            .toList();
        if (tags.isEmpty) tags = null;
      }

      final result = await service.publishPost(
        title: _titleController.text,
        content: _contentController.text,
        status: _status,
        categories: categories,
        tags: tags,
        excerpt: _excerptController.text,
      );

      setState(() {
        _isPublishing = false;
      });

      if (result['success'] == true) {
        final data = result['data'];
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text('发布成功'),
            content: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('文章ID: ${data['id']}'),
                Text('标题: ${data['title']['rendered']}'),
                Text('状态: ${data['status']}'),
              ],
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: const Text('确定'),
              ),
            ],
          ),
        );

        // 清空表单
        if (_formKey.currentState != null) { // 添加非空检查
          _formKey.currentState!.reset();
        }
        _titleController.clear();
        _contentController.clear();
        _categoriesController.clear();
        _tagsController.clear();
        _excerptController.clear();
        setState(() {
          _status = 'draft';
        });
      } else {
        showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: const Text('发布失败'),
            content: Text(result['error']),
            actions: [
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: const Text('确定'),
              ),
            ],
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('发布文章'),
      ),
      body: _isPublishing
          ? const Center(child: CircularProgressIndicator())
          : Padding(
              padding: const EdgeInsets.all(16.0),
              child: Form(
                key: _formKey,
                child: ListView(
                  children: [
                    TextFormField(
                      controller: _titleController,
                      decoration: const InputDecoration(
                        labelText: '文章标题',
                      ),
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return '请输入文章标题';
                        }
                        return null;
                      },
                    ),
                    const SizedBox(height: 16),
                    TextFormField(
                      controller: _contentController,
                      decoration: const InputDecoration(
                        labelText: 'HTML内容',
                        alignLabelWithHint: true,
                      ),
                      maxLines: 10,
                      validator: (value) {
                        if (value == null || value.isEmpty) {
                          return '请输入文章内容';
                        }
                        return null;
                      },
                    ),
                    const SizedBox(height: 16),
                    DropdownButtonFormField<String>(
                      value: _status,
                      decoration: const InputDecoration(
                        labelText: '发布状态',
                      ),
                      items: const [
                        DropdownMenuItem(
                          value: 'draft',
                          child: Text('草稿'),
                        ),
                        DropdownMenuItem(
                          value: 'publish',
                          child: Text('发布'),
                        ),
                      ],
                      onChanged: (value) {
                        setState(() {
                          _status = value!;
                        });
                      },
                    ),
                    const SizedBox(height: 16),
                    TextFormField(
                      controller: _categoriesController,
                      decoration: const InputDecoration(
                        labelText: '分类ID (多个用逗号分隔)',
                      ),
                      keyboardType: TextInputType.number,
                    ),
                    const SizedBox(height: 16),
                    TextFormField(
                      controller: _tagsController,
                      decoration: const InputDecoration(
                        labelText: '标签ID (多个用逗号分隔)',
                      ),
                      keyboardType: TextInputType.number,
                    ),
                    const SizedBox(height: 16),
                    TextFormField(
                      controller: _excerptController,
                      decoration: const InputDecoration(
                        labelText: '文章摘要',
                      ),
                      maxLines: 3,
                    ),
                    const SizedBox(height: 24),
                    ElevatedButton(
                      onPressed: _publishPost,
                      child: const Text('发布文章'),
                    ),
                  ],
                ),
              ),
            ),
    );
  }
}

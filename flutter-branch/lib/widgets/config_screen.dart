import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../models/wordpress_config.dart';

class ConfigScreen extends StatefulWidget {
  final Function(WordPressConfig) onConfigSaved;

  const ConfigScreen({Key? key, required this.onConfigSaved}) : super(key: key);

  @override
  _ConfigScreenState createState() => _ConfigScreenState();
}

class _ConfigScreenState extends State<ConfigScreen> {
  final _formKey = GlobalKey<FormState>();
  final _siteUrlController = TextEditingController();
  final _usernameController = TextEditingController();
  final _appPasswordController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _loadSavedConfig();
  }

  Future<void> _loadSavedConfig() async {
    final prefs = await SharedPreferences.getInstance();
    final siteUrl = prefs.getString('siteUrl') ?? '';
    final username = prefs.getString('username') ?? '';
    final appPassword = prefs.getString('appPassword') ?? '';

    setState(() {
      _siteUrlController.text = siteUrl;
      _usernameController.text = username;
      _appPasswordController.text = appPassword;
    });
  }

  Future<void> _saveConfig() async {
    if (_formKey.currentState!.validate()) {
      final config = WordPressConfig(
        siteUrl: _siteUrlController.text,
        username: _usernameController.text,
        appPassword: _appPasswordController.text,
      );

      // 保存到SharedPreferences
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('siteUrl', config.siteUrl);
      await prefs.setString('username', config.username);
      await prefs.setString('appPassword', config.appPassword);

      // 通知父组件
      widget.onConfigSaved(config);

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('配置已保存')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('WordPress配置'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _siteUrlController,
                decoration: const InputDecoration(
                  labelText: 'WordPress站点URL',
                  hintText: 'https://yourwordpresssite.com',
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return '请输入站点URL';
                  }
                  if (!value.startsWith('http')) {
                    return '请输入有效的URL';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _usernameController,
                decoration: const InputDecoration(
                  labelText: '用户名',
                ),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return '请输入用户名';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: _appPasswordController,
                decoration: const InputDecoration(
                  labelText: '应用程序密码',
                ),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return '请输入应用程序密码';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: _saveConfig,
                child: const Text('保存配置'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
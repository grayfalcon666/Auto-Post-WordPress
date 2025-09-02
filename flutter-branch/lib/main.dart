import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'models/wordpress_config.dart';
import 'widgets/config_screen.dart';
import 'widgets/publish_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'WordPress发布工具',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  WordPressConfig? _config;

  @override
  void initState() {
    super.initState();
    _loadConfig();
  }

  Future<void> _loadConfig() async {
    final prefs = await SharedPreferences.getInstance();
    final siteUrl = prefs.getString('siteUrl');
    final username = prefs.getString('username');
    final appPassword = prefs.getString('appPassword');

    if (siteUrl != null && username != null && appPassword != null) {
      setState(() {
        _config = WordPressConfig(
          siteUrl: siteUrl,
          username: username,
          appPassword: appPassword,
        );
      });
    }
  }

  void _handleConfigSaved(WordPressConfig config) {
    setState(() {
      _config = config;
    });
    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('WordPress发布工具'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (_config == null)
              const Text(
                '请先配置WordPress连接信息',
                style: TextStyle(fontSize: 18),
              )
            else
              Column(
                children: [
                  const Text(
                    '已配置WordPress连接',
                    style: TextStyle(fontSize: 18),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '站点: ${_config!.siteUrl}',
                    style: const TextStyle(fontSize: 14),
                  ),
                  Text(
                    '用户: ${_config!.username}',
                    style: const TextStyle(fontSize: 14),
                  ),
                ],
              ),
            const SizedBox(height: 24),
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => ConfigScreen(
                      onConfigSaved: _handleConfigSaved,
                    ),
                  ),
                );
              },
              child: const Text('配置WordPress'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _config == null
                  ? null
                  : () {
                      Navigator.of(context).push(
                        MaterialPageRoute(
                          builder: (context) => PublishScreen(config: _config!),
                        ),
                      );
                    },
              child: const Text('发布文章'),
            ),
          ],
        ),
      ),
    );
  }
}
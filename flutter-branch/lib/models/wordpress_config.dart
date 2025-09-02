class WordPressConfig {
  String siteUrl;
  String username;
  String appPassword;

  WordPressConfig({
    required this.siteUrl,
    required this.username,
    required this.appPassword,
  });

  Map<String, dynamic> toMap() {
    return {
      'siteUrl': siteUrl,
      'username': username,
      'appPassword': appPassword,
    };
  }

  static WordPressConfig fromMap(Map<String, dynamic> map) {
    return WordPressConfig(
      siteUrl: map['siteUrl'],
      username: map['username'],
      appPassword: map['appPassword'],
    );
  }

  bool get isValid {
    return siteUrl.isNotEmpty && username.isNotEmpty && appPassword.isNotEmpty;
  }
}
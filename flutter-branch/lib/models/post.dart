class WordPressPost {
  final String title;        // 文章标题
  final String content;      // 文章内容（HTML格式）
  final String status;       // 状态：publish（发布）/ draft（草稿）
  final List<int>? categories; // 分类ID列表（可选）
  final List<int>? tags;     // 标签ID列表（可选）
  final String? excerpt;     // 文章摘要（可选）

  WordPressPost({
    required this.title,
    required this.content,
    required this.status,
    this.categories,
    this.tags,
    this.excerpt,
  });

  // 转API请求体（WordPress REST API格式）
  Map<String, dynamic> toApiBody() => {
        'title': title,
        'content': content,
        'status': status,
        if (categories != null && categories!.isNotEmpty) 'categories': categories,
        if (tags != null && tags!.isNotEmpty) 'tags': tags,
        if (excerpt != null && excerpt!.isNotEmpty) 'excerpt': excerpt,
      };
}
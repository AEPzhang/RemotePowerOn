# FastAPI Project

![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/yourusername/yourrepo/main.yml?style=flat-square) ![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

一个基于FastAPI构建的RESTful API项目，使用Python开发。

## ✨ 功能特性

- 用户认证（JWT）
- CRUD操作示例
- 异步请求支持
- Swagger UI自动文档（/docs）
- 单元测试覆盖
- Docker容器化支持
- 环境变量配置

## 🚀 快速开始

### 前置要求

- Python 3.9+
- PyCharm（推荐）或其他Python IDE
- pip 21.0+

### 安装步骤

1. 克隆仓库：
   ```bash
   git clone https://github.com/AEPzhang/RemotePowerOn.git
   cd yourrepo
   ```

2. 创建虚拟环境（PyCharm会自动创建）：
   ```bash
    python -m venv venv
    # 激活虚拟环境：
    # Windows: venv\Scripts\activate
    # Unix/macOS: source venv/bin/activate
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 运行开发服务器
   ```bash
   uvicorn main:app --reload
   ```
   访问以下端点：
   
   - API文档：[http://localhost:8000/docs](http://localhost:8000/docs)
   - 备用文档：[http://localhost:8000/redoc](http://localhost:8000/redoc)

### ⚙️ 配置
创建 `.env` 文件（参考 `.env.example`）：
```env
APP_ENV=development
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
```

### 🧪 运行测试
```bash
pytest -v
```

### 🐳 Docker部署
构建镜像：
```bash
docker build -t fastapi-app .
```
运行容器：
```bash
docker run -d -p 8000:8000 --name myapp fastapi-app
```

### 📂 项目结构
```
.
├── app
│   ├── api
│   │   └── v1
│   │       └── endpoints
│   ├── core
│   ├── models
│   └── schemas
├── tests
├── requirements.txt
├── Dockerfile
└── main.py
```

### 🤝 贡献指南
1. Fork项目仓库
2. 创建特性分支 (git checkout -b feature/AmazingFeature)
3. 提交更改 (git commit -m 'Add some AmazingFeature')
4. 推送分支 (git push origin feature/AmazingFeature)
5. 创建Pull Request

### 📄 许可证
MIT License - 详见 LICENSE 文件

Happy Coding! 🎉

### 使用说明：
1. 将"yourusername/yourrepo"替换为您的实际仓库信息
2. 根据实际项目需求修改功能特性部分
3. 如果使用数据库，请补充数据库配置说明
4. 添加项目特定的API端点文档
5. 更新测试部分的说明（如果有特殊测试需求）
6. 添加项目相关的截图或演示GIF（如果需要）

建议在PyCharm中：
- 启用Python虚拟环境
- 配置运行配置为`uvicorn main:app --reload`
- 安装Python插件和FastAPI插件以获得更好的代码提示
``` 

请根据你的具体项目情况替换占位符，并调整相应的内容。
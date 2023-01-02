import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()
    setuptools.setup(
        name='nonebot-plugin-bilibili-image',
        version='0.0.2.1',
        author='jcjrobert',
        author_email='jcjrobbie@gmail.com',
        keywords=["pip", "nonebot2", "nonebot", "bilibili"],
        url='https://github.com/jcjrobert/nonebot-plugin-bilibili-image',
        description='b站图片下载',
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Programming Language :: Python :: 3',
        ],
        license='AGPL-3.0 license',
        packages=setuptools.find_packages(),
        include_package_data=True,
        platforms="any",
        install_requires=[
            'nonebot2>=2.0.0-beta.4', 'nonebot-adapter-onebot>=2.0.0-beta.4', 'httpx>=0.19.0', 'beautifulsoup4>=4.0.0'
        ]
    )
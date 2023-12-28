# SJTU选课自动检漏脚本
## 使用方法
1. 打开选课界面，保证所在页面可以搜索到自己想检漏的课程；
2. 在refresh,sh文件第10行“echo '人工智能的数学基础' | xsel -i -b”中，将echo后面引号内的内容替换为自己目标课程的名字；
3. 在项目目录下打开命令行，运行 python auto.py；
4. 鼠标单击网页页面，确保网页正在刷新；
5. 等待检漏即可。每次的检测结果都输出在logs/log文件中。"green not detected"表示选课人数是红色，即选满； "green detected"表示人数是绿色，即未选满；
6. 如果想确认截图区域是否正确截取到了待选课程的选课人数数字，可以在auto.py文件中将“绘制截图”部分代码注释去掉，通过调整left,top,width,height来确保输出截图区域正确。在命令行中使用 xdotool getmouselocation 命令可以获取当前鼠标的位置。

## 项目技术方案
- OpenCV进行颜色识别
- xdotool实现自动操作鼠标和键盘
- xsel操作剪贴板
### 加入剪贴板操作
保证剪贴板粘贴的始终是自己想检的课，使用了linux系统级package xsel实现。
详情可见：https://bbs.huaweicloud.com/blogs/311385

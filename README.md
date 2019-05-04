## Handbook of InsPointer

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2p9qe4rarj31f20gctb3.jpg)

In 21 century, if you want to become excellent, you must have your own works. InsPointer is a tool to track your works. It seems like `git`, when you're going to write or have written some things, you can generate an unique identification code, and add it to your work, the work will be track by InsPointer.

The work will be a slice of evernote, a list in workflowy, or a commit of code.

Now, it's just a minimum viable product, developed by python. I imagine that in the future a datebase will store all your works using the unique data. You just need to write and generate, Inspointer will help you to track them all.

卓越需要作品。InsPointer 就是一个追踪作品的工具。它的工作原理像`git`一样，当你完成一样作品时，只需要简单的操作Inspointer，就可以生成一个唯一的id用来追踪这个作品。作品可以是一篇以碎片形式出现的`印象笔记`，也可以是写在`workflowy`里的一段list，或者是本地或者远程的一段代码，等等。

现在，`InsPointer`只是一个用python开发的最小可用产品，我设想将来他可以自动把你所有添加指针的作品，都放到你自己的专有数据库中，你只需要完成作品，添加指针，`InsPointer`会自动帮你把这些作品抓取到数据库中。


### How can I use it

This is an Alfred tool which can generate an unique identification code, and record it as `.csv`. The record is bind with recording time, and using time.

Firstly, if you have Alfred, you should download the alfred workflow [by click](https://www.github.com/) . Then install it.

Then you can call out Alfred and input `inspointer` and the time which you use in creating. Such as this:

![](https://ws2.sinaimg.cn/large/006tNc79gy1g2pf37xx5lg30go04kk17.gif)

When you click `Enter`, the unique code will be copied to your clipboard, like this:

```
/*/*/ Using 300 min work on 68ed557d-6e4f-11e9-a392-acbc32acd253
```

第一个版本是一个alfred的workflow插件，他会生成一个独特的id，并记录你完成作品需要的时间和当下的时间点。

首先，如果你有Alfred，那么[点击下载](https://www.github.com/),然后双击安装。之后，呼出Alfred的输入框，输入`InsPointer`和完成作品所需的时间，就像上面的图那样。

最后，插件会帮你把唯一编码复制到剪贴板，粘贴即可。

### If you are interested in

If you're interested in this tool. You can check the origin code in this repository. Or if you want to connect with me or want to develop this tool with me. You can folk this repository and connect me by 1@showidea.cn

如果你对这个工具感兴趣，可以直接在仓库中查看源代码，如果你想一起把这个工具做得更好，你可以folk这个仓库，或者联系我 1@showidea.cn，希望能够与志同道合的小伙伴一起交流。

### Changelog

2019.5.4：hechengyuan init repository.

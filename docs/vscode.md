# 1. VSCode Plugins
```
Visual Studio IntelliCode
Ansible
Beautify
Docker
flask-snippets
Kubernetes
Python
Vetur
vscode-icons
vuetify-vscode
YAML
Debugger for Chrome
Indent-Rainbow
Prettier
Bracket Pair Colorizer
CSS Peek
Python Preview
Live Share
Color Picker
Vue i18n Ally
Go
JavaScript and TypeScript Nightly
Latest TypeScript and Javascript Grammar
Oracle Developer Tools for VS 
Debugger for Firefox 
Git History
SQLTools - Database tools
Debugger for Microsoft Edge
C/C++
C#
Remote - SSH
Remote - Containers
Node Debug
Remote Development
Maven for Java
Prettier - Code formatter
TSLint
markdownlint
docs-markdown
markdown pdf
```

# 2. Go Development
```go
go get -u -v github.com/bytbox/golint 
go get -u -v github.com/golang/tools 
go get -u -v github.com/lukehoban/go-outline 
go get -u -v github.com/newhook/go-symbols 
go get -u -v github.com/mdempsky/gocode 
go get -u -v github.com/uudashr/gopkgs/v2/cmd/gopkgs 
go get -u -v github.com/ramya-rao-a/go-outline 
go get -u -v github.com/acroca/go-symbols 
go get -u -v golang.org/x/tools/cmd/guru 
go get -u -v golang.org/x/tools/cmd/gorename 
go get -u -v github.com/cweill/gotests
go get -u -v github.com/fatih/gomodifytags 
go get -u -v github.com/josharian/impl 
go get -u -v github.com/davidrjenni/reftools/cmd/fillstruct 
go get -u -v github.com/haya14busa/goplay/cmd/goplay 
go get -u -v github.com/godoctor/godoctor 
go get -u -v github.com/go-delve/delve/cmd/dlv 
go get -u -v github.com/stamblerre/gocode 
go get -u -v github.com/rogpeppe/godef 
go get -u -v github.com/sqs/goreturns 
go get -u -v golang.org/x/lint/golint 
go get -u -v github.com/gin-gonic/gin
go get -u -v golang.org/x/tools/gopls 

或者

go get -v github.com/bytbox/golint 
go get -v github.com/golang/tools 
go get -v github.com/lukehoban/go-outline 
go get -v github.com/newhook/go-symbols 
go get -v github.com/mdempsky/gocode 
go get -v github.com/uudashr/gopkgs/v2/cmd/gopkgs 
go get -v github.com/ramya-rao-a/go-outline 
go get -v github.com/acroca/go-symbols 
go get -v golang.org/x/tools/cmd/guru 
go get -v golang.org/x/tools/cmd/gorename 
go get -v github.com/cweill/gotests
go get -v github.com/fatih/gomodifytags 
go get -v github.com/josharian/impl 
go get -v github.com/davidrjenni/reftools/cmd/fillstruct 
go get -v github.com/haya14busa/goplay/cmd/goplay 
go get -v github.com/godoctor/godoctor 
go get -v github.com/go-delve/delve/cmd/dlv 
go get -v github.com/stamblerre/gocode 
go get -v github.com/rogpeppe/godef 
go get -v github.com/sqs/goreturns 
go get -v golang.org/x/lint/golint 
go get -v github.com/gin-gonic/gin
go get -v golang.org/x/tools/gopls 
```

# 3. Git代理
```bash
git config --global http.proxy socks5://127.0.0.1:7070
http_proxy=socks5://127.0.0.1:7070 go get xxxx

#恢復重置git配置：
git config --global --unset http.proxy

export http_proxy=socks5://127.0.0.1:1080
export https_proxy=$http_proxy

# go 1.11可以使用GOPROXY
export GOPROXY=https://goproxy.io
```

# 4. Go代理
## 4.1 Git&go get 使用 Shadowsocks 代理

- Linux/Mac

```bash
export http_proxy="http://127.0.0.1:1080"
export https_proxy="http://127.0.0.1:1080"

# Socks5
export http_proxy="socks5://127.0.0.1:1080"
export https_proxy="socks5://127.0.0.1:1080"
```

- Windows

```powershell
set http_proxy="http://127.0.0.1:1080"
set https_proxy="http://127.0.0.1:1080"

# Socks5
set http_proxy="socks5://127.0.0.1:1080"
set https_proxy="socks5://127.0.0.1:1080"

# 或
$env:http_proxy="http://127.0.0.1:1080"
$env:https_proxy="http://127.0.0.1:1080"

# Socks5
$env:http_proxy="socks5://127.0.0.1:1080"
$env:https_proxy="socks5://127.0.0.1:1080"
```

## 4.2 go get 使用 goproxy

- Go 1.13 及以上（推荐）

```go
$ go env -w GO111MODULE=on
$ go env -w GOPROXY=https://goproxy.cn,direct
```

- Linux/Mac (如果您使用的 Go 版本是 1.12 及以下)

```bash
$ export GO111MODULE=on
$ export GOPROXY=https://goproxy.cn

或

$ echo "export GO111MODULE=on" >> ~/.profile
$ echo "export GOPROXY=https://goproxy.cn" >> ~/.profile
$ source ~/.profile
```

- Windows (如果您使用的 Go 版本是 1.12 及以下)

```powershell
C:\> $env:GO111MODULE = "on"
C:\> $env:GOPROXY = "https://goproxy.cn"

或

1. 打开“开始”并搜索“env”
2. 选择“编辑系统环境变量”
3. 点击“环境变量…”按钮
4. 在“<你的用户名> 的用户变量”章节下（上半部分）
5. 点击“新建…”按钮
6. 选择“变量名”输入框并输入“GO111MODULE”
7. 选择“变量值”输入框并输入“on”
8. 点击“确定”按钮
9. 点击“新建…”按钮
10. 选择“变量名”输入框并输入“GOPROXY”
11. 选择“变量值”输入框并输入“https://goproxy.cn”
12. 点击“确定”按钮
```

- 自托管 Go 模块代理

你的代码永远只属于你自己，因此我们向你提供目前世界上最炫酷的自托管 Go 模块代理搭建方案。通过使用 Goproxy 这个极简主义项目，你可以在现有的任意 Web 服务中轻松地加入 Go 模块代理支持，要知道 goproxy.cn 就是基于它搭建的。

创建一个名为 goproxy.go 的文件

```go
package main

import (
    "net/http"
    "os"

    "github.com/goproxy/goproxy"
)

func main() {
    g := goproxy.New()
    g.GoBinEnv = append(
        os.Environ(),
        "GOPROXY=https://goproxy.cn,direct", // 使用 goproxy.cn 作为上游代理
        "GOPRIVATE=git.example.com",         // 解决私有模块的拉取问题（比如可以配置成公司内部的代码源）
    )
    http.ListenAndServe("localhost:8080", g)
}
```

并且运行它

```
$ go run goproxy.go
```

然后通过把 GOPROXY 设置为 http://localhost:8080 来试用它。另外，我们也建议你把 GO111MODULE 设置为 on。

就这么简单，一个功能完备的 Go 模块代理就搭建成功了。事实上，你可以将 Goproxy 结合着你钟爱的 Web 框架一起使用，比如 Gin 和 Echo，你所需要做的只是多添加一条路由而已。更高级的用法请查看文档。

- 常用 GOPROXY

```
https://goproxy.baidu.com
https://goproxy.cn
https://goproxy.io
https://mirrors.aliyun.com/goproxy/
https://gonexus.dev
https://athens.azurefd.net
https://gocenter.io
https://proxy.golang.org
```

## 4.3 go module

- Linux/Mac

```bash
export GO111MODULE=on
```

- Windows

```powershell
set GO111MODULE=on
```

## 4.4 安装 VSCode 的 Go 开发依赖包

```bash
go get -u -v github.com/bytbox/golint
go get -u -v github.com/golang/tools
go get -u -v github.com/lukehoban/go-outline
go get -u -v github.com/newhook/go-symbols
go get -u -v github.com/mdempsky/gocode
go get -u -v github.com/uudashr/gopkgs/v2/cmd/gopkgs
go get -u -v github.com/ramya-rao-a/go-outline
go get -u -v github.com/acroca/go-symbols
go get -u -v golang.org/x/tools/cmd/guru
go get -u -v golang.org/x/tools/cmd/gorename
go get -u -v github.com/cweill/gotests
go get -u -v github.com/fatih/gomodifytags
go get -u -v github.com/josharian/impl
go get -u -v github.com/davidrjenni/reftools/cmd/fillstruct
go get -u -v github.com/haya14busa/goplay/cmd/goplay
go get -u -v github.com/godoctor/godoctor
go get -u -v github.com/go-delve/delve/cmd/dlv
go get -u -v github.com/stamblerre/gocode
go get -u -v github.com/rogpeppe/godef
go get -u -v github.com/sqs/goreturns
go get -u -v golang.org/x/lint/golint
go get -u -v github.com/gin-gonic/gin
go get -u -v golang.org/x/tools/gopls
```

```bash
go install github.com/bytbox/golint
go install github.com/golang/tools
go install github.com/lukehoban/go-outline
go install github.com/newhook/go-symbols
go install github.com/mdempsky/gocode
go install github.com/uudashr/gopkgs/v2/cmd/gopkgs
go install github.com/ramya-rao-a/go-outline
go install github.com/acroca/go-symbols
go install golang.org/x/tools/cmd/guru
go install golang.org/x/tools/cmd/gorename
go install github.com/cweill/gotests
go install github.com/fatih/gomodifytags
go install github.com/josharian/impl
go install github.com/davidrjenni/reftools/cmd/fillstruct
go install github.com/haya14busa/goplay/cmd/goplay
go install github.com/godoctor/godoctor
go install github.com/go-delve/delve/cmd/dlv
go install github.com/stamblerre/gocode
go install github.com/rogpeppe/godef
go install github.com/sqs/goreturns
go install golang.org/x/lint/golint
go install github.com/gin-gonic/gin
go install golang.org/x/tools/gopls
```

## 4.5 安装 beego 框架和 bee 工具

```powershell
go get -u github.com/astaxie/beego
go get -u github.com/beego/bee
```

```powershell
go install github.com/astaxie/beego
go install github.com/beego/bee
```

## 4.6 Q&A

Q1. git 或 go get 的其他包源码无法同步到自建的 github repository？

> A1. 删除下载的 repository 下的".git"文件夹。

# 5.VSCode Snnipets
## 5.1 Python Snnipets
```json
//python.json
{
    // Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
    // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
    // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
    // same ids are connected.
    // Example:
    // "Print to console": {
    //  "prefix": "log",
    //  "body": [
    //      "console.log('$1');",
    //      "$2"
    //  ],
    //  "description": "Log output to console"
    // }

    "HEADER": {
        "prefix": "header",
        "body": [
            "# -*- encoding: utf-8 -*-",
            "'''",
            "@File    :   $TM_FILENAME",
            "@Time    :   $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
            "@Author  :   Abelit ",
            "@Version :   1.0",
            "@Contact :   ychenid@live.com",
            "@Copyright :   (C)Copyright 2020, dataforum.org",
            "@Licence :   BSD-3-Clause",
            "@Desc    :   None",
            "'''",
            "",
            "",
            "$0"
        ],
    }
}
```

## 5.2 Vue/Javascript/Typescript/ES6

```json
// vue.json
{
    // Place your snippets for vue here. Each snippet is defined under a snippet name and has a prefix, body and 
    // description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
    // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
    // same ids are connected.
    // Example:
    // "Print to console": {
    //  "prefix": "log",
    //  "body": [
    //      "console.log('$1');",
    //      "$2"
    //  ],
    //  "description": "Log output to console"
    // }
    "Print to console": {
        "prefix": "vue",
        "body": [
            "<template>",
            "    <div>\n",
            "    </div>",
            "</template>\n",
            "<script>",
            "export default {",
            "    name: '$1',",
            "    props: {\n",
            "    },",
            "    components: {\n",
            "    },",
            "    data() {",
            "        return {\n",
            "        };",
            "    },",
            "    computed: {\n",
            "    },",
            "    created() {\n",
            "    },",
            "    mounted() {\n",
            "    },",
            "    watch: {\n",
            "    },",
            "    methods: {\n",
            "    },",
            "};",
            "</script>\n",
            "<style scoped lang=\"${1:scss}\">",
            "    /* @import url(); 引入css类 */\n",
            "</style>\n",
        ],
        "description": "Create vue template"
    },
    "Vue Component": {
        "prefix": "vuets",
        "description": "Vue component snippet",
        "body": [
            "<template>",
            "    <div>\n",
            "    </div>",
            "</template>\n",
            "",
            "<script lang=\"ts\">",
            "import { Component, Prop, Vue } from 'vue-property-decorator';",
            "",
            "@Component",
            "export default class ${1:ComponentName} extends Vue {",
            "\t@Prop() private msg!: string;\n",
            "",
            "}",
            "</script>",
            "",
            "<style scoped lang=\"${1:scss}\">",
            "    /* @import url(); 引入css类 */\n",
            "</style>\n",
            ""
        ]
    },
    "Vue standard API (SFC)": {
        "prefix": "vbase",
        "body": [
            "<template>",
            "\t<div>",
            "",
            "\t</div>",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue from \"vue\";",
            "",
            "\texport default Vue.extend({",
            "\t\t${0}",
            "\t});",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base for Vue.js File with TypeScript"
    },
    "VueConstructor standard API (SFC)": {
        "prefix": "vcbase",
        "body": [
            "<template>",
            "\t<div>",
            "",
            "\t</div>",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue, { VueConstructor } from \"vue\";",
            "",
            "\texport default (Vue as VueConstructor<Vue>).extend({",
            "\t\t${0}",
            "\t});",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base with VueConstructor for Vue.js File with TypeScript"
    },
    "VueConstructor standard API extending interface (SFC)": {
        "prefix": "vcibase",
        "body": [
            "<template>",
            "\t<div>",
            "",
            "\t</div>",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue, { VueConstructor } from \"vue\";",
            "\timport ${1:NameComponent} from \"@/components/${1:NameComponent}.vue\";",
            "",
            "\tinterface Refs {",
            "\t\t\\$refs: {",
            "\t\t\t${2:aliasComponent}: InstanceType<typeof ${1:NameComponent}>,",
            "\t\t}",
            "\t}",
            "\texport default (Vue as VueConstructor<Vue & Refs>).extend({",
            "\t\t${0}",
            "\t});",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base with VueConstructor extending interface for Vue.js File with TypeScript"
    },
    "Class-style API Vue (SFC)": {
        "prefix": "vcsbase",
        "body": [
            "<template>",
            "\t<div>",
            "",
            "\t</div>",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue from \"vue\";",
            "\timport Component from \"vue-class-component\";",
            "",
            "\t@Component({})",
            "\texport default class ${1:App} extends Vue {",
            "\t\t${0}",
            "\t};",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base class-style API for Vue.js File with TypeScript"
    },
    "Class-style API Vue extending Props (SFC)": {
        "prefix": "vcsibase",
        "body": [
            "<template>",
            "\t<div>",
            "",
            "\t</div>",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue from \"vue\";",
            "\timport Component from \"vue-class-component\";",
            "",
            "\tconst ${1:App}Props = Vue.extend({",
            "\t\tprops: {",
            "\t\t\t${2:nameProp}: ${3:type}",
            "\t\t}",
            "\t})",
            "",
            "\t@Component({})",
            "\texport default class ${1:App} extends ${1:App}Props {",
            "\t\t${0}",
            "\t};",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base class-style API extending Props for Vue.js File with TypeScript"
    },
    "Vue Composition API using Vue 2": {
        "prefix": "vcompbase",
        "body": [
            "<template>",
            "",
            "</template>",
            "",
            "<script lang=\"ts\">",
            "\timport Vue from \"vue\";",
            "\timport { defineComponent } from \"@vue/composition-api\";",
            "",
            "\texport default defineComponent({",
            "\t\t${0}",
            "\t});",
            "</script>",
            "",
            "<style scoped>",
            "",
            "</style>"
        ],
        "description": "Base for Vue.js File with TypeScript using the Composition API plugin for Vue 2"
    }
}
```

# 6. VSCode Settings
## 6.1 Latex/TexWorkshop
settings.json
```json
{
    // Latex workshop
    "latex-workshop.latex.tools": [
          {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
            ]
          },
          {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
              ]
          },          
          {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
            ]
          },
          {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
            "%DOCFILE%"
            ]
          }
        ],
    "latex-workshop.latex.recipes": [
          {
            "name": "xelatex",
            "tools": [
            "xelatex"
                        ]
                  },
          {
            "name": "latexmk",
            "tools": [
            "latexmk"
                        ]
          },

          {
            "name": "pdflatex -> bibtex -> pdflatex*2",
            "tools": [
            "pdflatex",
            "bibtex",
            "pdflatex",
            "pdflatex"
                        ]
          }
        ],
    "latex-workshop.view.pdf.viewer": "tab",  
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
      ]
}
```

## 6.2 Typescript Settings

```json
// tslint.json
{
  "defaultSeverity": "warning",
  "extends": [
    "tslint:recommended"
  ],
  "linterOptions": {
    "exclude": [
      "node_modules/**"
    ]
  },
  "rules": {
    "indent": [
      true,
      "spaces",
      2
    ],
    "interface-name": false,
    "no-consecutive-blank-lines": false,
    "object-literal-sort-keys": false,
    "ordered-imports": false,
    "arrow-parens": [
      false,
      "as-needed"
    ],
    "quotemark": [
      true,
      "single"
    ],
    "semicolon": [
      true,
      "always",
      "ignore-interfaces"
    ],
    "trailing-comma": [
      true,
      {
        "singleline": "never",
        "multiline": {
          "objects": "ignore",
          "arrays": "ignore",
          "functions": "never",
          "typeLiterals": "ignore"
        }
      }
    ],
    "no-console": false,
    "prefer-const": false,
    "object-literal-key-quotes": [
      false,
      "consistent-as-needed"
    ]
  }
}
```

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
    "strict": true,
    "jsx": "preserve",
    "importHelpers": true,
    "moduleResolution": "node",
    "experimentalDecorators": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "sourceMap": true,
    "baseUrl": ".",
    "types": [
      "webpack-env",
      "jest"
    ],
    "paths": {
      "@/*": [
        "src/*"
      ]
    },
    "lib": [
      "esnext",
      "dom",
      "dom.iterable",
      "scripthost"
    ]
  },
  "include": [
    "src/**/*.ts",
    "src/**/*.tsx",
    "src/**/*.vue",
    "tests/**/*.ts",
    "tests/**/*.tsx"
  ],
  "exclude": [
    "node_modules"
  ],
  // support comment in json file
  "files.associations": {
    "tslint.json": "jsonc"
  }
}
```

# 7.Font Settings
## 7.1 Operator Mono

- Install Operator Mono Font
```bash
cp ./fonts/OperatorMono/* /usr/share/fonts/truetype/operator-mono/
mkfontscale
fc-cache -fv
```

- Configure VSCode
```json
{
    "git.autofetch": true,
    "[vue]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "go.useLanguageServer": true,
    "window.zoomLevel": 0,
    "latex-workshop.view.pdf.viewer": "browser",
    "explorer.confirmDelete": false,
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "python.languageServer": "Microsoft",
    "[typescriptreact]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "typescript.updateImportsOnFileMove.enabled": "always",
    "editor.quickSuggestions": {
        "strings": true
    },
    "[typescript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "beautify.config": "",
    "editor.fontFamily": "Operator Mono",
    "editor.fontSize": 15,
    "editor.fontLigatures": true, // 这个控制是否启用字体连字，true启用，false不启用，这里选择启用
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "name": "italic font",
                "scope": [
                    "comment",
                    "keyword",
                    "storage",
                    "keyword.control.import",
                    "keyword.control.default",
                    "keyword.control.from",
                    "keyword.operator.new",
                    "keyword.control.export",
                    "keyword.control.flow",
                    "storage.type.class",
                    "storage.type.function",
                    "storage.type",
                    "storage.type.class",
                    "variable.language",
                    "variable.language.super",
                    "variable.language.this",
                    "meta.class",
                    "meta.var.expr",
                    "constant.language.null",
                    "support.type.primitive",
                    "entity.name.method.js",
                    "entity.other.attribute-name",
                    "punctuation.definition.comment",
                    "text.html.basic entity.other.attribute-name.html",
                    "text.html.basic entity.other.attribute-name",
                    "tag.decorator.js entity.name.tag.js",
                    "tag.decorator.js punctuation.definition.tag.js",
                    "source.js constant.other.object.key.js string.unquoted.label.js",
                ],
                "settings": {
                    "fontStyle": "italic",
                }
            },
        ]
    }
}
```
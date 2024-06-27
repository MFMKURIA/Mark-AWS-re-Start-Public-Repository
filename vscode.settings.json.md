{
  // Editor settings
  "editor.guides.bracketPairs": true, // Enable bracket pair guides
  "editor.fontSize": 14, // Set editor font size
  "editor.minimap.enabled": true, // Enable minimap
  "editor.wordWrap": "off", // Disable word wrap
  "editor.renderWhitespace": "all", // Render all whitespaces
  "editor.formatOnSave": true, // Format on save
  "editor.snippetSuggestions": "inline", // Show snippet suggestions inline
  "editor.inlineSuggest.suppressSuggestions": true, // Suppress inline suggestions
  "editor.tabSize": 4, // Sets tab size to 4 spaces
  "editor.rulers": [80, 100, 120], // Sets visual guidelines at 80, 100, and 120 characters
  "editor.quickSuggestions": {
    "other": true, // Enable suggestions for other contexts
    "comments": false, // Disable suggestions within comments
    "strings": true // Enable suggestions within strings
  }, // Configures quick suggestions behavior
  "editor.bracketPairColorization.enabled": true, // Enables bracket pair colorization for improved code readability
  "editor.codeActionsOnSave": { 
    "source.organizeImports": "always", // Automatically organizes imports
    "source.fixAll": "always", // Fixes all auto-fixable problems
  }, // Configures actions to run on file save

  // Error Lens extension settings
  "errorLens.enabled": true, // Enables Error Lens to highlight errors in the editor
  "errorLens.fontWeight": "bold", // Sets font weight for Error Lens annotations
  "errorLens.fontSize": "14px", // Sets font size for Error Lens annotations

  // Live Share extension settings
  "liveshare.featureSet": "insiders", // Enables Live Share Insiders for real-time collaboration

  // Privacy extension for VSCode
  "Codegeex.Privacy": true,

  // Terminal settings
  "terminal.integrated.fontSize": 14, // Set terminal font size
  "terminal.integrated.cursorBlinking": true, // Enable cursor blinking

  // File settings
  "files.autoSave": "onFocusChange", // Auto save files on focus change
  "explorer.confirmDelete": true, // Confirm before deleting files

  // Extension settings
  "extensions.autoUpdate": true, // Auto update extensions

  // TabNine settings
  "tabnine.experimentalAutoImports": true, // Enable experimental auto imports for TabNine

  // Breadcrumbs settings
  "breadcrumbs.enabled": true, // Enable breadcrumbs

  // cSpell settings
  "cSpell.userWords": [
    "autofetch",
    "Codegeex",
    "docstrings",
    "drawio",
    "hediet",
    "javac",
    "liveshare",
    "Pylance",
    "tabnine",
    "whitespaces",
    "yourusername"
  ], // Custom words for spell checking

  // Git settings
  "git.autofetch": true, // Auto fetch git repositories

  // Python settings
  "python.formatting.provider": "black", // Use Black as the formatter
  "python.languageServer": "Pylance", // Use Pylance as the language server
  "python.analysis.typeCheckingMode": "strict", // Enable strict type checking
  "python.analysis.diagnosticSeverityOverrides": {
    "reportUnboundVariable": "information",
    "reportImplicitStringConcatenation": "warning"
  }, // Override diagnostic severity levels
  "python.analysis.autoImportCompletions": true, // Enable auto import completions
  "python.analysis.autoFormatStrings": true, // Auto format strings

  // Black formatter settings
  "editor.defaultFormatter": "ms-python.black-formatter", // Set default formatter to Black
  "black-formatter.args": [
    "--line-length",
    "88"
  ], // Set line length for Black formatter
  "black-formatter.cwd": "${workspaceFolder}", // Set working directory for Black formatter
  "black-formatter.path": [
    "black"
  ], // Path to Black formatter
  "black-formatter.interpreter": [
    "python"
  ], // Path to Python interpreter
  "black-formatter.importStrategy": "useBundled", // Use bundled Black formatter
  "black-formatter.showNotification": "onError", // Show notifications on error
  "black-formatter.serverTransport": "stdio", // Use stdio for communication

  // CSS settings
  "css.enabledLanguages": [
    "html"
  ], // Enable CSS for HTML

  // Workbench settings
  "workbench.colorTheme": "Visual Studio Dark", // Set color theme
  "workbench.iconTheme": "vscode-icons", // Set icon theme
  "workbench.editorAssociations": {
    "*.svg": "hediet.vscode-drawio-text"
  }, // Associate SVG files with draw.io extension

  // Auto Close Tag settings
  "auto-close-tag.enableAutoCloseTag": true, // Enable auto close tag
  "auto-close-tag.enableAutoCloseSelfClosingTag": true, // Enable auto close self-closing tag
  "auto-close-tag.insertSpaceBeforeSelfClosingTag": false, // Disable space before self-closing tag
  "auto-close-tag.activationOnLanguage": [
    "xml",
    "python",
    "php",
    "blade",
    "ejs",
    "jinja",
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact",
    "plaintext",
    "markdown",
    "vue",
    "liquid",
    "erb",
    "lang-cfml",
    "cfml",
    "HTML (EEx)",
    "HTML (Eex)",
    "plist"
  ], // Activate on specific languages
  "auto-close-tag.disableOnLanguage": [], // Disable on specific languages
  "auto-close-tag.excludedTags": [
    "area",
    "base",
    "br",
    "col",
    "command",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr"
  ], // Exclude specific tags
  "auto-close-tag.SublimeText3Mode": true, // Enable Sublime Text 3 mode
  "auto-close-tag.fullMode": true, // Enable full mode

  // Auto Comment Blocks settings
  "auto-comment-blocks.singleLineBlockOnEnter": true, // Insert new commented line on Enter
  "auto-comment-blocks.disabledLanguages": [], // Disable comment completion for specific languages
  "auto-comment-blocks.slashStyleBlocks": [
    "c",
    "cpp",
    "csharp",
    "fsharp",
    "go",
    "groovy",
    "java",
    "javascript",
    "less",
    "objective-c",
    "php",
    "rust",
    "sass",
    "swift",
    "typescript"
  ], // Enable '//' and '///' style blocks for specific languages
  "auto-comment-blocks.hashStyleBlocks": [
    "coffeescript",
    "dockerfile",
    "makefile",
    "perl",
    "powershell",
    "python",
    "r",
    "ruby",
    "yaml"
  ], // Enable '#' style blocks for specific languages
  "auto-comment-blocks.semicolonStyleBlocks": [
    "clojure"
  ], // Enable ';' style blocks for specific languages

  // Editor Semantic Token Color Customizations
  "editor.semanticTokenColorCustomizations": {
    "[One Dark Pro]": {
      "enabled": true,
      "rules": {
        "magicFunction:python": "#ee0000",
        "*.decorator:python": "#0000dd",
        "*.typeHint:python": "#5500aa"
      }
    }
  }, // Customize semantic token colors

  // Auto Docstring settings
  "autoDocstring.docstringFormat": "google", // Set docstring format to Google
  "autoDocstring.generateDocstringOnEnter": true, // Generate docstring on Enter
  "autoDocstring.includeExtendedSummary": true, // Include extended summary
  "autoDocstring.guessTypes": true, // Guess types
  "autoDocstring.customTemplatePath": "/path/to/custom/template.mustache", // Custom template path
  "autoDocstring.quoteStyle": "'''", // Set quote style for docstrings

  // Code Runner settings
  "code-runner.executorMap": {
    "javascript": "node",
    "php": "C:\\php\\php.exe",
    "python": "python",
    "perl": "perl",
    "ruby": "C:\\Ruby23-x64\\bin\\ruby.exe",
    "go": "go run",
    "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
    "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
  }, // Set executor map for Code Runner
  "code-runner.customCommand": "echo Hello", // Custom command for Code Runner
  "code-runner.runInTerminal": true, // Run code in terminal

  // TypeScript and JavaScript settings
  "typescript.suggest.paths": false, // Disable path suggestions for TypeScript
  "javascript.suggest.paths": false, // Disable path suggestions for JavaScript

  // Path Intellisense settings
  "path-intellisense.extensionOnImport": true, // Enable extension on import
  "path-intellisense.showHiddenFiles": true, // Show hidden files
  "path-intellisense.autoSlashAfterDirectory": true, // Auto slash after directory
  "path-intellisense.autoTriggerNextSuggestion": true, // Auto trigger next suggestion
  "path-intellisense.absolutePathToWorkspace": true, // Absolute path to workspace
  "path-intellisense.mappings": {
    "/": "${workspaceFolder}",
    "lib": "${workspaceFolder}/lib",
    "global": "/Users/yourusername/globalLibs"
  }, // Path mappings
}
module.exports = (grunt) ->
  grunt.loadNpmTasks "grunt-contrib-coffee"
  grunt.loadNpmTasks "grunt-contrib-watch"
  grunt.loadNpmTasks "grunt-contrib-uglify"
  grunt.loadNpmTasks "grunt-contrib-sass"
  grunt.loadNpmTasks "grunt-contrib-concat"

  # Change base only after loading npm tasks
  srcBase = grunt.option('srcBase')

  grunt.initConfig

    #Compile coffeescript files
    coffee:
      sourceMap: true
      app:
        src: [ "#{srcBase}/static-src/coffee/**.coffee" ]
        dest: "#{srcBase}/static-src/CACHE/app.js"

    #Concatenate all javascript libfiles into a single slug
    #Assumes individual files are already minified (no further uglification/minification)
    concat:
      options:
        separator: ';'
        stripBanners: true
      libjs:
        src: [ "#{srcBase}/static/lib/**.js" ]
        dest: "#{srcBase}/static/compiled-js/lib.js"
      libcss:
        src: [ "#{srcBase}/static/lib/**.css" ]
        dest: "#{srcBase}/static/compiled-css/lib.css"

    #Compile SASS files
    sass:
      all:
        sourcemap: false
        style: 'compressed'
        files:[
          {
            expand: true
            cwd: "#{srcBase}/static-src/sass/"
            src: ["app.sass", "bootstrap.scss", "fontawesome/font-awesome.scss"]
            dest: "#{srcBase}/static/compiled-css/"
            ext: ".css"
          }
        ]

    #Published uglified version of compiled app.js
    uglify:
      options:
        mangle: false
        compress: false
        beautify: true
      app:
        src: [ "#{srcBase}/static-src/CACHE/app.js" ]
        dest: "#{srcBase}/static/compiled-js/app.js"

    # Watch relevant source files and perform tasks when they change
    watch:
      appScripts:
        files: [ "#{srcBase}/static-src/coffee/**.coffee" ]
        tasks: [ "coffee:app", "uglify:app" ]

      appStyle:
        files: [ "#{srcBase}/static-src/s[ac]ss/**/**.s[ac]ss" ]
        tasks: [ "sass:all" ]

      libScripts:
        files: [ "#{srcBase}/static/lib/**.js" ]
        tasks: [ "concat:libjs" ]
      libStyles:
        files: [ "#{srcBase}/static/lib/**.css" ]
        tasks: [ "concat:libcss" ]

  grunt.registerTask "default", ['coffee:app', 'sass:all', 'uglify:app', 'concat']

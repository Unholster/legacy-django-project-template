module.exports = (grunt) ->
  grunt.initConfig

    #Compile coffeescript files
    coffee:
      sourceMap: true
      app:
        src: [ "./static-src/coffee/**.coffee" ]
        dest: "./static-src/CACHE/app.js"

    #Concatenate all javascript libfiles into a single slug
    #Assumes individual files are already minified (no further uglification/minification)
    concat:
      options:
        separator: ';'
        stripBanners: true
      dist:
        src: [ "./static/lib/**.js" ]
        dest: "./static/compiled-js/lib.js"

    #Published uglified version of compiled app.js
    uglify:
      options:
        mangle: false
        compress: false
        beautify: true
      app:
        src: [ "./static-src/CACHE/app.js" ]
        dest: "./static/compiled-js/app.js"

    # Watch relevant source files and perform tasks when they change
    watch:
      appScripts:
        files: [ "./static-src/coffee/**.coffee" ]
        tasks: [ "coffee:app", "uglify:app" ]

      appStyle:
        files: [ "./static-src/s[ac]ss/**.s[ac]ss" ]
        tasks: [ "sass:app" , "sass:dist"]

      libScripts:
        files: [ "./static/lib/**.js" ]
        tasks: [ "concat:dist" ]


  grunt.loadNpmTasks "grunt-contrib-coffee"
  grunt.loadNpmTasks "grunt-contrib-watch"
  grunt.loadNpmTasks "grunt-contrib-uglify"
  grunt.loadNpmTasks "grunt-contrib-sass"
  grunt.loadNpmTasks "grunt-contrib-concat"
  grunt.registerTask "default", ['coffee:app', 'sass:app', 'sass:dist', 'uglify:app', 'concat:dist']

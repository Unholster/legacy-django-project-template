project = "{{project_name}}"

module.exports = (grunt) ->
  grunt.initConfig
    
    #Compile coffeescript files
    coffee:
      sourceMap: false
      app:
        src: [ "../#{project}/static-src/coffee/**.coffee" ]
        dest: "../#{project}/static-src/CACHE/app.js"

    #Concatenate all javascript libfiles into a single slug
    #Assumes individual files are already minified (no further uglification/minification)
    concat:
      lib:
        separator: ';'
        stripBanners: true
        src: [ "../{{project}}/static/lib/**.js" ]
        dest: "../{{project}}/static/lib.js"
      
    #Compile SASS files
    sass:
      app:
        sourcemap: false
        style: 'compressed'
        src: [ "../#{project}/static-src/sass/**.sass" ]
        dest: "../#{project}/static/compiled-css/app.css"

    #Published uglified version of compiled app.js
    uglify:
      app:
        src: [ "../#{project}/static-src/CACHE/app.js" ]
        dest: "../#{project}/static/compiled-js/app.js"

    # Watch relevant source files and perform tasks when they change
    watch:
      appScripts:
        files: [ "../#{project}/static-src/coffee/**.coffee" ]
        tasks: [ "coffee:app", "uglify:app" ]

      appStyle:
        files: [ "../#{project}/static-src/sass/**.sass" ]
        tasks: [ "sass:app" ]

      libScripts:
        files: [ "../{{project}}/static/lib/**.js" ]
        tasks: [ "concat:lib" ]


  grunt.loadNpmTasks "grunt-contrib-coffee"
  grunt.loadNpmTasks "grunt-contrib-watch"
  grunt.loadNpmTasks "grunt-contrib-uglify"
  grunt.loadNpmTasks "grunt-contrib-sass"
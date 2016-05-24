// 'use strict';
 
// var gulp = require('gulp');
// var sass = require('gulp-sass');
 
// gulp.task('sass', function () {
//   return gulp.src('static/**/*.scss')
//     .pipe(sass().on('error', sass.logError))
//     .pipe(gulp.dest('./css/'));
// });
 
// gulp.task('watch', function () {
//   gulp.watch('**/*.scss', ['sass']);
// });

// gulp.task("default", ["sass", "watch"]);


var gulp = require('gulp');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var notify = require("gulp-notify");
var concat = require('gulp-concat');
var rename = require("gulp-rename");


gulp.task('sass', function() {
    return gulp.src('homepage/static/css/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({
            follow: true
        }))
        .pipe(sourcemaps.write('./maps'))
        .pipe(rename(function(path){
            path.extname = ".min" + path.extname;
            return path;
        }))
        .pipe(gulp.dest('dist'))
        .pipe(notify("Built SASS!"));
});


gulp.task('scripts', function() {
  return gulp.src('static/js/**/*.js')
    .pipe(concat('app.min.js'))
    .pipe(gulp.dest('dist/js'));
});


gulp.task('watch', function() {
    gulp.watch('homepage/static/css', ['sass']);
    gulp.watch('**/*.js', ['scripts']);
});

gulp.task("default", ["sass", "scripts"]);

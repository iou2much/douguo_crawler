'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp',['angular-loading-bar','ngAnimate','begriffs.paginate-anything'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
      cfpLoadingBarProvider.includeSpinner = false;
      cfpLoadingBarProvider.latencyThreshold = 50;
  }]);
  
phonecatApp.controller('CloudCtrl', function($scope, $http,$window) {
  $http.get('/static/data/word_cloud.json').success(function(data) {
    var fill = d3.scale.category20();
    
    data = data.slice(0,100);
    
    d3.layout.cloud().size([$("#cloud_div").width()-200, 400])
        .words(data)
        .padding(4)
        .timeInterval(10)
        //.rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw)
        .start();
    //function setQuery(q){
    
    function draw(words) {
      //console.log($scope);
      $window.scope = $scope;
      //console.log($window);
      //d3.select("body").append("svg")
      d3.select("#cloud_div").append("svg")
          .attr("width", $('#cloud_div').width())//+1600)
          //.attr("width", 800)//$('#cloud_div').width()+600)
          .attr("height", 400)
          .attr("viewbox", "0 0 1000 1500")
          .append("g")
          .attr("margin-left", 200)
          .attr("width", $('#cloud_div').width())//+1600)
          .attr("height", 400)
          //.attr("style", "fill:red")
          //.attr("transform", "translate(150,150)")
          .attr("transform", "translate(450,160)")
          .selectAll("text")
          .data(words)
          .enter().append("text")
          .style("font-size", function(d) { return d.size + "px"; })
          .style("font-family", "Impact")
          .style("cursor", "pointer")
          .style("fill", function(d, i) { return fill(i); })
          .attr("text-anchor", "middle")
          //.attr("onclick", "window.location.href='/static/gallery.html?q='+$(this).text();")
          .attr("onclick", "setQuery($(this).text())")
          //.attr("onclick", function(d,i){ return (function a(){$scope.query=d.text;})()})
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; })
          .append("set")
          .attr("attributeName",'font-size')
          .attr("from",function(d){return d.size})
          .attr("to",function(d){return d.size+3})
          .attr("begin",'mouseover')
          .attr("end",'mouseout');
    }
  });
  $scope.desc = true;
  $scope.query = '饼干';
});
function getDocHeight() {
    return Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );
}
phonecatApp.directive("bnLazySrc",bnLazySrc);

window.setQuery = function(q){
  //console.log(q);
  //console.log(window);
  //console.log(window.scope);
  window.scope.query = q;
  window.scope.$apply();
  $('#query').val(q);
}

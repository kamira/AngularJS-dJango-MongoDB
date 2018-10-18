var app = angular.module('myApp', []);

var post_url = 'http://localhost:8000/POST/'

app.controller('MainCtrl', ['$scope', '$http', function($scope, $http) {
  $scope.user = {};
  $scope.update = function(user) {
    console.log(user)
    rdyToPost = {'MODE': 'INSERT', 'DATA': angular.copy(user) }
    if (checkValue(rdyToPost)){
    	$scope.master = rdyToPost;
		rdyToPost['SCHE'] = 'user';
		$http({
            method: 'POST',
			headers: {
				'Content-Type': 'multipart/form-data'
			},
            url: post_url,
			contentType: 'application/json; charset=UTF-8',
            dataType: "json",
            data: JSON.stringify(rdyToPost),
			crossDomain: true
        })
		.success(function(response){
			alert(response['MSG']);
		})
		.error(function(response){
			alert(response['MSG']);
		});
    }
  };

  $scope.reset = function() {
    $scope.user = {};
    $scope.master = {};
  };

  $scope.reset();
}]);


function checkValue(json){
	data = json.DATA;
  
  return true;
  
  
}

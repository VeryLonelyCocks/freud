app.config(function($routeProvider, $locationProvider) {

  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  });

  $routeProvider
    .when('/', {
      controller: 'IndexController',
      templateUrl: '/src/pages/index/index.tpl.html'
    })
    .otherwise({
      redirect: '/'
    })

})
Rails.application.routes.draw do
  root to: 'pages#balancer'
  #get '/',  to: 'pages#balancer'
  get 'pages/balancer', to: 'pages#balancer'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end

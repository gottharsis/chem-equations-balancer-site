require File.join(Rails.root, "lib", "equation")
class PagesController < ApplicationController
  def balancer
    @b = (params[:eqn] == nil) ? nil : solve(params[:eqn])
  end
end

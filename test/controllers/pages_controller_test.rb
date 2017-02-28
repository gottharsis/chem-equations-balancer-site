require 'test_helper'

class PagesControllerTest < ActionDispatch::IntegrationTest
  test "should get balancer" do
    get pages_balancer_url
    assert_response :success
  end

end

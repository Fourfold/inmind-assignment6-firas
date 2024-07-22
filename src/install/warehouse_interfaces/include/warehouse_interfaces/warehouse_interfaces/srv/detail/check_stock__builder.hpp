// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from warehouse_interfaces:srv/CheckStock.idl
// generated code does not contain a copyright notice

#ifndef WAREHOUSE_INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_
#define WAREHOUSE_INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "warehouse_interfaces/srv/detail/check_stock__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace warehouse_interfaces
{

namespace srv
{

namespace builder
{

class Init_CheckStock_Request_item_name
{
public:
  Init_CheckStock_Request_item_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::warehouse_interfaces::srv::CheckStock_Request item_name(::warehouse_interfaces::srv::CheckStock_Request::_item_name_type arg)
  {
    msg_.item_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::warehouse_interfaces::srv::CheckStock_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::warehouse_interfaces::srv::CheckStock_Request>()
{
  return warehouse_interfaces::srv::builder::Init_CheckStock_Request_item_name();
}

}  // namespace warehouse_interfaces


namespace warehouse_interfaces
{

namespace srv
{

namespace builder
{

class Init_CheckStock_Response_stock_level
{
public:
  Init_CheckStock_Response_stock_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::warehouse_interfaces::srv::CheckStock_Response stock_level(::warehouse_interfaces::srv::CheckStock_Response::_stock_level_type arg)
  {
    msg_.stock_level = std::move(arg);
    return std::move(msg_);
  }

private:
  ::warehouse_interfaces::srv::CheckStock_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::warehouse_interfaces::srv::CheckStock_Response>()
{
  return warehouse_interfaces::srv::builder::Init_CheckStock_Response_stock_level();
}

}  // namespace warehouse_interfaces

#endif  // WAREHOUSE_INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_

console.log("상세페이지")

var price_for_js = document.getElementById("price_for_js").value;
console.log("상품가격 : ", price_for_js)

var name_for_js = document.getElementById("name_for_js").value;
console.log("상품 이름 : ", name_for_js)

let price;
price = price_for_js
console.log(price)

let selected_color;
    selected_color = document.getElementById("selected_color");

let entire_order;
entire_order = document.getElementById("entire_order");

let order_list;
order_list = document.getElementById("order_list");

let add_br;
add_br = document.createElement('br');

selected_color.addEventListener('change',function(){
    let add_order = document.createElement('div');
    var element_exist = document.getElementById(selected_color.value+'_order')
    console.log(element_exist)
    if (element_exist==null){
        add_order.setAttribute('id', selected_color.value+'_order')
        add_order.setAttribute('class', 'add_order')
        add_order.setAttribute('name', name_for_js+selected_color.value)
        order_list.appendChild(add_order);

        let added_order;
        added_order = document.getElementById(selected_color.value+'_order')
    
        add_span = document.createElement('span');
        add_span.append(selected_color.value)
        added_order.appendChild(add_span)
        
        let order_amount = document.createElement('input')
        order_amount.setAttribute('type', 'number')
        order_amount.setAttribute('id', selected_color.value+'_amount')
        order_amount.setAttribute("name", selected_color.value+'_amount')
        order_amount.setAttribute('value', 1)
        order_amount.setAttribute("class",'order_amount')
        added_order.appendChild(order_amount)
        

    }else{
        window.alert("이미 선택된 색상입니다. 수량을 변경해주세요~")
    }

})

order_list.addEventListener('change', function(){
    let add_order = document.createElement('div');
    let order_amount = document.getElementsByClassName("order_amount").length;
    console.log(order_amount)
    add_order.append("dlfafdjklsdfjklfsdkjl")
    entire_order.appendChild(add_order)
    console.log("change")
})

console.log("상세페이지")

var price_for_js = document.getElementById("price_for_js").value;
console.log("상품가격 : ", price_for_js)

var name_for_js = document.getElementById("name_for_js").value;
console.log("상품 이름 : ", name_for_js)

let price;
price = price_for_js
console.log(price)

// 색상 선택 
let selected_color;
    selected_color = document.getElementById("selected_color");

// 전체 주문 div
let entire_order;
entire_order = document.getElementById("entire_order");

//각 주문
let order_list;
order_list = document.getElementById("order_list");

//한 줄 띄기!!!
let add_br;
add_br = document.createElement('br');

// 총 상품금액 기입란
let entire_order_wrap;
entire_order_wrap = document.getElementById('entire_order_wrap')

//색상 선택시 => 주문 리스트 목록에 추가, 전체 주문 목록에 추가
selected_color.addEventListener('change',function(){
    // div 생성
    let add_div = document.createElement('div');
    // 해당 색상이 order_list에 있는지 확인
    var element_exist = document.getElementById(selected_color.value+'_order')
    console.log(element_exist)
    if (element_exist==null){
        add_div.setAttribute('id', selected_color.value+'_order')
        add_div.setAttribute('class', 'add_order')
        add_div.setAttribute('name', name_for_js+selected_color.value)
        order_list.appendChild(add_div);

        let added_order;
        added_order = document.getElementById(selected_color.value+'_order')
    
        add_span = document.createElement('span');
        add_span.append(selected_color.value)
        added_order.appendChild(add_span)
        
        let order_amount;
        order_amount = document.createElement('input')
        order_amount.setAttribute('type', 'number')
        order_amount.setAttribute('id', selected_color.value+'_amount')
        order_amount.setAttribute("name", selected_color.value+'_amount')
        order_amount.setAttribute('value', 1)
        order_amount.setAttribute("class",'order_amount')
        order_amount.setAttribute("min","1")
        added_order.appendChild(order_amount)

        console.log("여기서부터얌~~")
        let entire_order;
        entire_order = document.getElementById("entire_order");
        console.log(entire_order)

        if (entire_order==null){
            let add_div = document.createElement('div');
            add_div.setAttribute('id', 'entire_order');
            add_div.append("총 상품 금액");
            entire_order_wrap.appendChild(add_div);

            add_div = document.createElement('div');
            add_div.setAttribute('id', 'entire_order_price');
            add_div.append(price)
            entire_order_wrap.appendChild(add_div)

        }else{
            console.log("zzzzz");
        }

        
    }else{
        window.alert("이미 선택된 색상입니다. 수량을 변경해주세요~")
    }
    let order_amount = document.querySelectorAll('.order_amount')
    let total_amount = 0;
    for (let cnt = 0; cnt < order_amount.length; cnt++){                
        var this_amount;
        this_amount = parseInt(order_amount[cnt].value);
        total_amount = total_amount + this_amount;
    }

    let total_price; 
    total_price = total_amount * price;
    total_price = parseInt(total_price);

    let entire_order_price;
    entire_order_price = document.getElementById("entire_order_price");
    entire_order_price.innerText = total_price;

})


order_list.addEventListener('change', function(){
    let order_amount = document.querySelectorAll('.order_amount')
    let total_amount = 0;
    for (let cnt = 0; cnt < order_amount.length; cnt++){
        
        var this_amount;
        this_amount = parseInt(order_amount[cnt].value);
        total_amount = total_amount + this_amount;

    }

    let total_price; 
    total_price = total_amount * price;
    total_price = parseInt(total_price);

    let entire_order_price;
    entire_order_price = document.getElementById("entire_order_price");
    entire_order_price.innerText = total_price;

})




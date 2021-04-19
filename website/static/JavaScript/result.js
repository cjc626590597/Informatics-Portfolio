int i = 0;
int len = len(data);
window.onload = function(){
    var lb = document.getElementById("left");
    var rb = document.getElementById("right");
    var name = document.getElementById("name");
    var price = document.getElementById("price");
    var factory = document.getElementById("factory");
    var screen = document.getElementById("screen");
    var operate = document.getElementById("operate");
    var resolution = document.getElementById("resolution");
    var frequency = document.getElementById("frequency");
    var kernel = document.getElementById("kernel");
    var RAM = document.getElementById("RAM");
    var ROM = document.getElementById("ROM");
    var battery = document.getElementById("battery");
    var rear = document.getElementById("rear");
    var front = document.getElementById("front");
//    var url = "https://pro-fd.zol-img.com.cn/t_s300x300c5/g2/M00/03/09/ChMlWV25ZQWINx-NAAEsLIMvaxEAAND1wJrxBUAASxE748.jpg";
    var brand = document.getElementById("brand");
    var type = document.getElementById("type");
    lb.onclick = function(){
    	if(i == 0)
    		i = l;
    	else
    		i -= 1;
        name.innerHTML = data[i].Phone_name; // "Xiaomi";
        price.innerHTML = data[i].Phone_price;
        factory.innerHTML = data[i].Phone_factory_system_kernel;
        screen.innerHTML = data[i].Phone_screen_size;
        operate.innerHTML = data[i].Phone_screen_size;
        resolution.innerHTML = data[i].Phone_resolution;
        frequency.innerHTML = data[i].Phone_frequency;
        kernel.innerHTML = data[i].Phone_kernel_num;
        RAM.innerHTML = data[i].Phone_RAM_capacity;
        ROM.innerHTML = data[i].Phone_ROM_capacity;
        battery.innerHTML = data[i].Phone_battery_capacity;
        rear.innerHTML = data[i].Phone_rear_camera;
        front.innerHTML = data[i].Phone_front_camera;
//        document.getElementById("url").src=url;
        document.getElementById("url").src=data[i].Phone_pic_URL;
        brand.innerHTML = data[i].Phone_brand;
        type.innerHTML = data[i].Phone_target_group;
    }
    rb.onclick = function(){
    	if(i == l-1)
    		i = 0;
    	else
    		i += 1;
//        price.innerHTML = 2930;
        name.innerHTML = data[i].Phone_name; // "Xiaomi";
        price.innerHTML = data[i].Phone_price;
        factory.innerHTML = data[i].Phone_factory_system_kernel;
        screen.innerHTML = data[i].Phone_screen_size;
        operate.innerHTML = data[i].Phone_screen_size;
        resolution.innerHTML = data[i].Phone_resolution;
        frequency.innerHTML = data[i].Phone_frequency;
        kernel.innerHTML = data[i].Phone_kernel_num;
        RAM.innerHTML = data[i].Phone_RAM_capacity;
        ROM.innerHTML = data[i].Phone_ROM_capacity;
        battery.innerHTML = data[i].Phone_battery_capacity;
        rear.innerHTML = data[i].Phone_rear_camera;
        front.innerHTML = data[i].Phone_front_camera;
        document.getElementById("url").src=data[i].Phone_pic_URL;
        brand.innerHTML = data[i].Phone_brand;
        type.innerHTML = data[i].Phone_target_group;
    }
}
$('select').on('contentChanged', function() {
    // re-initialize (update)
    $(this).material_select();
});

$('#id_area').change(function(){
	getShopList(this.value);
})

$('#id_shop').change(function(){
	getShopSpending(this.value);
})

function getShopList(areaId){ 
	$.ajax({   
		type: "GET",
		url: "/survey/getShopList?areaId="+areaId,       
		dataType:'json',   
		success: function(data,textStatus){
			var select = document.getElementById("id_shop");
			select.options.length = 0
			if(data.length > 0) {
				for ( i=0; i<data.length; i++ ) {   
					select.options[i] = new Option();   
					select.options[i].text = data[i].name;   
					select.options[i].value = data[i].shopId; 
				}
				// trigger event
    			$("#id_shop").trigger('contentChanged');
			}
		}    
	})   
}  

function getShopSpending(shopId){ 
	$.ajax({   
		type: "GET",
		url: "/survey/getShopSpending?shopId="+shopId,       
		dataType:'json',   
		success: function(data,textStatus){
			var select = document.getElementById("id_shop");
			
			$("input[name=spending][checked=checked]").prop('checked', false);
			if (data.value != undefined){
				value = data.value;
				$("input[name=spending][value=" + value + "]").prop('checked', true);  	
			} else {
				$("input[name=spending][value=0]").prop('checked', true);  	
			}

		}    
	})   
}  

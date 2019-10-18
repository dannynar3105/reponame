function GetBatchData() {
   		
   		$.ajax({
   			type: 'GET',
   			url: 'http://localhost:5000/list',
   			dataType: 'json',
   			contentType: 'application/json;charset=utf-8',
   			success: function(product) {
   				var products = JSON.parse(product.name);
//    				var names = product.d;
//    				alert(product);
				$.each(products, function(index, value) {
        		$('#lstObjects').append($('<option>').text(value).val(index));
    			});
					
            },
   			failure: function(error) {
   				 alert(error.d); 
   			}
   		});
   
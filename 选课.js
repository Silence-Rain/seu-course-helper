var a = setInterval(function(){
	$.ajax({ 
		async:false, 
		type:"post", 
		contentType:"application/json", 
		url:"runSelectclassSelectionAction.action?select_jxbbh="+'09014070201730000'+"&select_xkkclx="+'11'+"&select_jhkcdm="+'09014070', 
		data:"{}", 
		dataType:"json", 
		success:function(data){ 
			if(data.rso.isSuccess == 'false'){ 
				console.log("体系结构"+data.rso.errorStr); 
				return; 
			}
			else{ 
				console.log('已成功选择!');
				clearInterval(a);
			} 
		},
		fail: function(data){
			console.log("网络连接错误");
		}
	}); 
}, 500);
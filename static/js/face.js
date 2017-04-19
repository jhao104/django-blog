/*
*	评论表情渲染JS
*	@author:	小毛(微博：BUPT朱小毛)
*	@data:		2013年2月17日
*	@version:	1.0
*	@rely:		jQuery
*/
$(function(){
	/*
	*		参数说明
	*		baseUrl:	【字符串】表情路径的基地址
	*		pace:		【数字】表情弹出层淡入淡出的速度
	*		dir:		【数组】保存表情包文件夹名字
	*		text:		【二维数组】保存表情包title文字
	*		num:		【数组】保存表情包表情个数
	*		isExist:	【数组】保存表情是否加载过,对于加载过的表情包不重复请求。
	*/
	var emotion = {
		baseUrl:	'',
		pace:		100,
		dir:		['mr','ali','yc','bzmh'],
		text:[			/*表情包title文字，自己补充*/
			[
				'Q0','Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20',
				'Q21','Q22','Q23','Q24','Q25','Q26','Q27','Q28','Q29','Q30','Q31','Q32','Q33','Q34','Q35','Q36','Q37','Q38','Q39','Q40',
				'Q41','Q42','Q43','Q44','Q45','Q46','Q47','Q48','Q49','Q50','Q51','Q52','Q53','Q54','Q55','Q56','Q57','Q58','Q59','Q60',
				'Q61','Q62','Q63','Q64','Q65','Q66','Q67','Q68','Q69','Q70','Q71','Q72','Q73','Q74','Q75','Q76','Q77','Q78','Q79','Q80',
				'Q81','Q82','Q83','Q84','Q85','Q86','Q87','Q88','Q89','Q90','Q91','Q92','Q93','Q94','Q95','Q96','Q97','Q798','Q99','Q100'
			],
		[
				'ali_0','ali_1','ali_2','ali_3','ali_4','ali_5','ali_6','ali_7','ali_8','ali_9','ali_10','ali_11','ali_12','ali_13','ali_14','ali_15','ali_16','ali_17','ali_18','ali_19','ali_20',
				'ali_21','ali_22','ali_23','ali_24','ali_25','ali_26','ali_27','ali_28','ali_29','ali_30','ali_31','ali_32','ali_33','ali_34','ali_35','ali_36','ali_37','ali_38','ali_39','ali_40',
				'ali_41','ali_42','ali_43','ali_44','ali_45','ali_46','ali_47','ali_48','ali_49','ali_50','ali_51','ali_52','ali_53','ali_54','ali_55','ali_56','ali_57','ali_58','ali_59','ali_60',
				'ali_61','ali_62','ali_63','ali_64','ali_65','ali_66','ali_67','ali_68','ali_69','ali_70','ali_71','ali_72','ali_73','ali_74'
			],
		[
				'yc_0','yc_1','yc_2','yc_3','yc_4','yc_5','yc_6','yc_7','yc_8','yc_9','yc_10','yc_11','yc_12','yc_13','yc_14','yc_15','yc_16','yc_17','yc_18','yc_19','yc_20',
				'yc_21','yc_22','yc_23','yc_24','yc_25','yc_26','yc_27','yc_28','yc_29','yc_30','yc_31','yc_32','yc_33','yc_34','yc_35','yc_36','yc_37','yc_38','yc_39','yc_40',
				'yc_41','yc_42','yc_43','yc_44','yc_45','yc_46','yc_47','yc_48','yc_49','yc_50','yc_51','yc_52','yc_53','yc_54','yc_55','yc_56','yc_57','yc_58','yc_59','yc_60',
				'yc_61','yc_62','yc_63','yc_64','yc_65','yc_66','yc_67','yc_68','yc_69','yc_70','yc_71','yc_72','yc_73','yc_74'
			],
	
			[
				'测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试',
				'测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试',
				'测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试',
				'测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试',
				'测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试','测试'
			]
		],
		num:		[49,50,35,0],
		isExist:	[0,0,0,0],
		bind:	function(i){
			$("#face-area .face-ul").eq(i).find('.face-item').each(function(){
				$(this).bind('click',function(){
					emotion.insertText(document.getElementById('txaArticle'),'['+$(this).find('img').attr('title')+']');
					$('#face-area').fadeOut(emotion.pace);
				});
			});
		},
		/*加载表情包函数*/
		loadImg:function(i){
			var node = $("#face-area .face-ul").eq(i);
			for(var j = 0; j<emotion.num[i];j++){
				var domStr = 	'<li class="face-item">' + 
									'<img src="' + emotion.baseUrl + '../images/face/' + emotion.dir[i] + '/' + j + '.gif" alt="' + emotion.text[i][j] + 
									'" title="' + emotion.text[i][j] + '" />' +
								'</li>';
				$(domStr).appendTo(node);
			}
			emotion.isExist[i] = 1;
			emotion.bind(i);
		},
		/*在textarea里光标后面插入文字*/
		insertText:function(obj,str){
			obj.focus();
			if (document.selection) {
				var sel = document.selection.createRange();
				sel.text = str;
			} else if (typeof obj.selectionStart == 'number' && typeof obj.selectionEnd == 'number') {
				var startPos = obj.selectionStart,
					endPos = obj.selectionEnd,
					cursorPos = startPos,
					tmpStr = obj.value;
				obj.value = tmpStr.substring(0, startPos) + str + tmpStr.substring(endPos, tmpStr.length);
				cursorPos += str.length;
				obj.selectionStart = obj.selectionEnd = cursorPos;
			} else {
				obj.value += str;
			}
		},
		init:function(){
			$("#face-area > ul.face-tab > li > a").each(function(i){
				$(this).bind('click',function(){
					if( $(this).hasClass('selected-a') )
						return;
					if( emotion.isExist[i] == 0 ){
						emotion.loadImg(i);
					}
					$("#face-area > ul.face-tab > li > a.selected-a").removeClass('selected-a');
					$(this).addClass('selected-a');
					$('#face-area .face_selected').removeClass('face_selected').hide();
					$('#face-area .face-ul').eq(i).addClass('face_selected').show();
				});
			});
			/*绑定表情弹出按钮响应，初始化弹出默认表情。*/
			$("#face-btn a").bind('click',function(){
				if( emotion.isExist[0] == 0 ){
					emotion.loadImg(0);
				}
				var w = $(this).position();
				$('#face-area').css({left:w.left,top:w.top+30}).fadeIn(400);
			});
			/*绑定关闭按钮*/
			$('#face-area a.face-close').bind('click',function(){
				$('#face-area').fadeOut(emotion.pace);
			});
			/*绑定document点击事件，对target不在rl_bq弹出框上时执行rl_bq淡出，并阻止target在弹出按钮的响应。*/
			$(document).bind('click',function(e){
				var target = $(e.target);
				if( target.closest("#face-btn a").length == 1 )
					return;
				if( target.closest("#face-area").length == 0 ){
					$('#face-area').fadeOut(emotion.pace);
				}
			});
		}
	};
	emotion.init();	//调用初始化函数。
});

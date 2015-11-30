function ca(f_inc1, f_inc2, f_expens) {
	
	$.getJSON('http://localhost:8080/svcAtide?inc1=' + f_inc1 + '&inc2=' + f_inc2 + '&expens=' + f_expens, function(data) {
		
		document.getElementById("rev_1").value = data.rev_1;
		document.getElementById("rev_2").value = data.rev_2;
		document.getElementById("total_rev").value = data.total_rev;
		document.getElementById("expens").value = data.expens;
		document.getElementById("diff_tr_ex").value = data.diff_tr_ex;
		document.getElementById("prc_rev1").value = data.prc_rev1;
		document.getElementById("prc_rev2").value = data.prc_rev2;
		document.getElementById("prc_val_diff1").value = data.prc_val_diff1;
		document.getElementById("prc_val_diff2").value = data.prc_val_diff2;
		document.getElementById("prc_val_rev1").value = data.prc_val_rev1;
		document.getElementById("prc_val_rev2").value = data.prc_val_rev2;

	});
	
	$.mobile.changePage( "#resultDiv");
};


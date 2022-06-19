$(document).ready(function () {
    $('#enroll_start').datepicker('setStartDate', new Date()).on('changeDate', function (ev) {
        $(this).datepicker('hide');
    });

    $('#enroll_end').datepicker().on('changeDate', function (ev) {
        $(this).datepicker('hide');
    });

    $('#course_start').datepicker('setStartDate', new Date()).on('changeDate', function (ev) {
        $(this).datepicker('hide');
    });

    $('#course_end').datepicker().on('changeDate', function (ev) {
        $(this).datepicker('hide');
    });

    $('#enroll_start').on('change', function () {
        var enroll_start = $("#enroll_start").val();
        $('#enroll_end').datepicker('setStartDate', enroll_start);
    });

    $('#course_start').on('change', function () {
        var course_start = $("#course_start").val();
        $('#course_end').datepicker('setStartDate', course_start);
    });
});
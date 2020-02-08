   UIkit.util.on('#js-modal-confirm', 'click', function (e) {
           e.preventDefault();
           e.target.blur();
           UIkit.modal.confirm('Are you sure,you want to suspend ?').then(function () {
               window.location.replace(e.target.getAttribute('url'))
           }, function () {
               console.log('Rejected.')
           });
       });


      UIkit.util.on('#js-release-confirm', 'click', function (e) {
           e.preventDefault();
           e.target.blur();
           UIkit.modal.confirm('Are you sure release ?').then(function () {
               window.location.replace(e.target.getAttribute('url'))
           }, function () {
               console.log('Rejected.')
           });
       });

          UIkit.util.on('#teacher-delete-confirm', 'click', function (e) {
           e.preventDefault();
           e.target.blur();
           UIkit.modal.confirm('Are you sure ?').then(function () {
               window.location.replace(e.target.getAttribute('url'))
           }, function () {
               console.log('Rejected.')
           });
       });




      UIkit.util.on('#student_remove_from_class', 'click', function (e) {
           e.preventDefault();
           e.target.blur();
           UIkit.modal.confirm('Are you sure ?').then(function () {
               window.location.replace(e.target.getAttribute('url'))
           }, function () {
               console.log('Rejected.')
           });
       });

 UIkit.util.on('#student_remove_from_class_', 'click', function (e) {
           e.preventDefault();
           e.target.blur();
           UIkit.modal.confirm('Are you sure ?').then(function () {
               window.location.replace(e.target.getAttribute('url'))
           }, function () {
               console.log('Rejected.')
           });
       });


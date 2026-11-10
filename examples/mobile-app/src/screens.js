// Screen layout described as data, not runnable UI.
// A real React Native / Expo app would render these layouts with
// components; here the layout is plain data so it can be checked by
// tests without a device, emulator or build step.
'use strict';

const taskListScreen = {
  name: 'TaskList',
  title: 'Danh sách công việc',
  header: { title: 'Danh sách công việc' },
  form: {
    fields: [
      { id: 'title', label: 'Tên công việc', type: 'text', maxLength: 100, required: true },
    ],
    submitLabel: 'Thêm công việc',
  },
  list: {
    emptyText: 'Chưa có công việc nào.',
    itemLayout: [
      { part: 'title', style: 'strong' },
      { part: 'status', values: ['Chưa xong', 'Đã xong'] },
      { part: 'createdAt', format: 'date-vi-VN' },
    ],
  },
};

const taskDetailScreen = {
  name: 'TaskDetail',
  title: 'Chi tiết công việc',
  fields: [
    { id: 'title', label: 'Tên công việc' },
    { id: 'amount', label: 'Số tiền (đồng)', format: 'currency-VND' },
    { id: 'createdAt', label: 'Ngày tạo', format: 'date-vi-VN' },
  ],
};

module.exports = { taskListScreen, taskDetailScreen };

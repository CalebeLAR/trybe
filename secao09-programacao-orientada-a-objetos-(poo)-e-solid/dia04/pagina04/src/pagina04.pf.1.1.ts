export default function progressNotification(
  message: string,
  notificationType: string,
): void {
  if (notificationType) console.log(`${notificationType}: ${message}`);
  if (!notificationType) console.log(message);
}

const arr = [
  { message: 'Gmail_1', notificationType: 'Gmail_1' },
  { message: 'Gmail_2', notificationType: 'Gmail_2' },
  { message: 'Gmail_3', notificationType: 'Gmail_3' },
  { message: 'Gmail_4', notificationType: 'Gmail_4' },
  { message: 'Gmail_5', notificationType: 'Gmail_5' },
];

arr.forEach((not) => progressNotification(not.message, not.notificationType));
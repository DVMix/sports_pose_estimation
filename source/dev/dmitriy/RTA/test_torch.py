import torch.nn.functional as F
import torchvision as tv
import torchvision.transforms as transforms

import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import DataLoader
from torch.autograd import Variable


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        # Сверточный слой
        # i --> input channels
        # 6 --> output channels
        # 5 --> kernel size
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        # Полностью связанный слой
        # 16 * 4 * 4 --> input vector dimensions
        # 120 --> output vector dimensions
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Convolution-> ReLu-> Pooling
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))

        # reshape, «-1» означает адаптивный
        # x = (n * 16 * 4 * 4) --> n : input channels
        # x.size()[0] == n --> input channels
        x = x.view(x.size()[0], -1)

        # Полностью связанный слой
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x


def training():
    # Определить предварительную обработку данных
    transform = transforms.Compose([
        transforms.ToTensor(),  # Преобразовать в тензор и нормализовать до [0, 1]
    ])

    # Учебный комплект
    trainset = tv.datasets.MNIST(
        root='data/',
        train=True,
        download=True,
        transform=transform
    )
    trainloader = DataLoader(
        dataset=trainset,
        batch_size=4,
        shuffle=True
    )

    # Десять меток в наборе данных MNIST
    classes = ('0', '1', '2', '3', '4',
               '5', '6', '7', '8', '9')

    # Создать модель сети
    net = Net()

    if torch.cuda.is_available():
        # Используйте GPU
        net.cuda()

    # Определить функцию потерь и оптимизатор
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.005, momentum=0.9)

    for epoch in range(5):
        running_loss = 0.0
        for i, data in enumerate(trainloader):
            # Введите данные
            inputs, labels = data
            if torch.cuda.is_available():
                inputs = inputs.cuda()
                labels = labels.cuda()
            inputs, labels = Variable(inputs), Variable(labels)

            # Градиент очистить 0
            optimizer.zero_grad()

            # forward + backward
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()

            # Обновить параметры
            optimizer.step()

            # Распечатать информацию журнала
            running_loss += loss.item()

            # Печать статуса тренировки каждые 2000 партий
            if i % 100 == 99:
                print(
                    '[{}/{}][{}/{}] loss: {:.3f}'.format(epoch + 1, 5, (i + 1) * 4, len(trainset), running_loss / 100))
                running_loss = 0.0

        # Сохранить файл параметров
        torch.save(net.state_dict(), 'checkpoints/model_{}.pth'.format(epoch + 1))
        print('model_{}.pth saved'.format(epoch + 1))

    print('Finished Training')
    pass


if __name__ == '__main__':
    # training()
    tensor = torch.randn(size=(1, 1, 32, 32))
    conv1 = torch.nn.Conv2d(1, 3)


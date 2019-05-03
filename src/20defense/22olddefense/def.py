from module.trainer import Trainer

def main():
    trainer = Trainer()
    trainer.train()
    trainer.test() #mnist, font digit 95
    trainer.attack()
    trainer.defend()

if __name__ == '__main__':
    main()

//
//  ViewController.swift
//  SeguesGenericos
//
//  Created by CEDAM19 on 12/09/23.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet weak var interruptor: UISwitch!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


    @IBAction func IrAMorado(_ sender: Any) {
        if interruptor.isOn {
            performSegue(withIdentifier: "Morado", sender: nil)
        }
    }
    
    
    @IBAction func IrAAmarillo(_ sender: Any) {
        if interruptor.isOn {
            performSegue(withIdentifier: "Amarillo", sender: nil)
        }
    }
    
    @IBAction func regresarAPrincipal(unwindSegue: UIStoryboardSegue){
        
    }
}

